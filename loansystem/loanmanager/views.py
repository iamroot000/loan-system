from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from loan.models import loan_table, borrower_table, loan_payment
from .process.control import Manager
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

C = Manager()
# Create your views here.
class IndexView(View):

    def get(self, request):

        template = "loanmanager/index.html"

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

def get_request_table(request):

    loanTableDetails = loan_table.objects.filter(is_approved=False)
    data = list(loanTableDetails.values())
    print(data)

    return JsonResponse({'data': data})

#make condition catch for existing active borrower ( confirmation displaying )
#Number of activeloans
#add requestor
def add_loan(request):
    if request.method == 'POST':
        varName = request.POST.get('borrowerName')
        varAmountLoan = request.POST.get('loanAmount')
        varloanType = C.loan_method(request.POST.get('paymentMethod'))
        varAmountLeft = request.POST.get('loanWithPercent')
        varDaysLeft = request.POST.get('numberOfDays')
        varAmountPerDay = request.POST.get('amountPerDay')
        varLoanProfit = C.loan_profit(varAmountLoan)
        varTataProfit = C.staff_profit(varAmountLoan)
        varUser = request.user
        borrower_table_obj = borrower_table(name=varName)
        borrower_table_obj.save()
        loan_table_obj = loan_table(name=varName, loan_type=varloanType, amount_loan=varAmountLoan, total_days=varDaysLeft, days_left=varDaysLeft, amount_per_day=varAmountPerDay, amount_left=varAmountLeft, loan_profit=varLoanProfit, tata_profit=varTataProfit)
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
    loan_payment_obj = loan_payment.objects.filter(loan_id__loan_id=loan_id)
    dates_list = [{'dates_to_pay': payment.dates_to_pay, 'paid_dates': payment.paid_dates, 'paid': payment.paid} for payment in loan_payment_obj]
    data = {'details': details, 'payments': dates_list}
    return JsonResponse(data)
    # return HttpResponse('TEST')

def approve_loan(request):
    if request.method == 'POST':
        loan_id = int(request.POST.get('loanId'))
        loan_table_obj = get_object_or_404(loan_table, loan_id=loan_id)
        now = datetime.now()
        days_to_pay=loan_table_obj.total_days
        print(days_to_pay)
        for day in range(1, days_to_pay+1):
            # print(day)
            delta = timedelta(days=day)
            date = now + delta
            date_str = date.strftime("%Y-%m-%d")
            loan_payment_obj = loan_payment(loan_id=loan_table_obj,dates_to_pay=date_str)
            loan_payment_obj.save()
            print(date_str)
        dueDelta = timedelta(days=days_to_pay)
        dueDate = now + dueDelta
        
        loan_table_obj.start_date = now.strftime("%Y-%m-%d")
        loan_table_obj.due_date = dueDate.strftime("%Y-%m-%d")
        loan_table_obj.is_approved = True
        loan_table_obj.save()
        data = {'status': 'success', 'message': 'Loan Request has been sent'}
    else:
        data = {'status': 'error', 'message': 'Invalid request method.'}

    return JsonResponse(data)

def decline_loan(request):

    return HttpResponse('DECLINED')

#make an alert method for payment overdue
    