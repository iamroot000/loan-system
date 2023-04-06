from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from loan.models import loan_table, borrower_table, loan_payment, payment_request
from .process.control import Manager
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.db.models import F, Q 
import json

C = Manager()
# Create your views here.
class IndexView(View):

    def get(self, request):

        template = "loanmanager/index.html"
        #display currently logged in user
        #print(request.user.username)

        loanTableDetails = loan_table.objects.filter(is_approved=True)
        requestTableDetails = loan_table.objects.filter(is_approved=False)
        context = {
            'loanTableDetails': loanTableDetails,
            'requestTableDetails': requestTableDetails,
        }
        return render(request, template, context)

def get_loan_table(request):

    loanTableDetails = loan_table.objects.filter(is_approved=True)
    data = list(loanTableDetails.values())
    print(data)

    return JsonResponse({'data': data})

#make condition catch for existing active borrower ( confirmation displaying )
#Number of activeloans
#add requestor
def add_loan(request):
    if request.method == 'POST':
        varName = request.POST.get('borrowerName')
        varAmountLoan = int(request.POST.get('loanAmount'))
        varloanType = C.loan_method(request.POST.get('paymentMethod'))
        varAmountLeft = request.POST.get('loanWithPercent')
        varDaysLeft = request.POST.get('numberOfDays')
        varAmountPerDay = request.POST.get('amountPerDay')
        varLoanProfit = C.loan_profit(varAmountLoan)
        varTataProfit = C.staff_profit(varAmountLoan)
        varUser = request.user
        borrower_table_obj = borrower_table(name=varName)
        # print(borrower_table_obj.active_loans)
        # print(type(borrower_table_obj.active_loans))
        plus_current_active_loan = int(borrower_table_obj.active_loans) + 1
        borrower_table_obj.active_loans = plus_current_active_loan
        borrower_table_obj.save()
        loan_table_obj = loan_table(name=varName, loan_type=varloanType, amount_loan=varAmountLoan, total_days=varDaysLeft, days_left=varDaysLeft, amount_per_day=varAmountPerDay, amount_left=varAmountLeft, loan_profit=varLoanProfit, tata_profit=varTataProfit, staff=request.user.username)
        loan_table_obj.save()

        print(varUser)

        data = {'status': 'success', 'message': 'Loan Request has been sent'}
    else:
        data = {'status': 'error', 'message': 'Invalid request method.'}

    return JsonResponse(data)

def get_borrower_details(request,loan_id):
    borrowerDetails = loan_table.objects.filter(loan_id=loan_id)
    details = list(borrowerDetails.values())
    # This query with "__" is for foreignkey
    # loan_payment_obj = loan_payment.objects.filter(loan_id__loan_id=loan_id)
    loan_payment_obj = loan_payment.objects.filter(loan_id__loan_id=loan_id).order_by(F('id').asc())
    dates_list = [{'dates_to_pay': payment.dates_to_pay, 'paid_dates': payment.paid_dates, 'paid': payment.paid} for payment in loan_payment_obj]
    data = {'details': details, 'payments': dates_list}
    return JsonResponse(data)
    # return HttpResponse('TEST')

def submit_payment_request(request):
    if request.method == 'POST':
        dat = json.loads(request.body)
        loan_id = dat.get('loan_id')
        borrower = dat.get('borrower')
        auditor = request.user.username 
        list_of_paid_dates = dat.get('list_of_paid_dates')
        amount_per_day = dat.get('amount_per_day')
        total_amount = amount_per_day * len(list_of_paid_dates)
        request_date = datetime.now()

        if list_of_paid_dates:
        # get all loan_payment objects with paid dates in list_of_paid_dates
            loan_payment_obj = loan_payment.objects.filter(
                Q(loan_id__loan_id=loan_id) & 
                Q(dates_to_pay__in=list_of_paid_dates)
            ).order_by('id')

            print(loan_payment_obj)

            for obj in loan_payment_obj:
                obj.paid_dates = request_date
                obj.save()

            payment_request_obj = payment_request(loan_id=loan_id, staff_name=auditor, dates_request=list_of_paid_dates, amount=total_amount, borrower_name=borrower)
            payment_request_obj.save()


        data = {'status': 'success', 'message': 'Loan Request has been sent'}
    else:
        data = {'status': 'error', 'message': 'Invalid request method.'}
    return JsonResponse(data)

#make an alert method for payment overdue