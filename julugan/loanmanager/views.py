from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from loanmanager.models import loan_table, loan_payment, payment_request
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

# Create your views here.
class IndexView(View):

    def get(self, request):
        template = "loanmanager/index.html"
        getRequestTableDetails = loan_table.objects.filter(is_approved=False)
        getRequestPaymentDetails = payment_request.objects.filter(is_approved=False)
        context = {
            'getRequestTableDetails': getRequestTableDetails,
            'getRequestPaymentDetails': getRequestPaymentDetails,
        }
        return render(request, template, context)
    
def approve_loan(request):
    if request.method == 'POST':
        loan_id = request.POST.get('loanId')
        loan_table_obj = get_object_or_404(loan_table, loan_id=loan_id)
        now = datetime.now()
        days_to_pay=loan_table_obj.total_days
        print(days_to_pay)
        for day in range(1, days_to_pay+1):
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
        data = {'status': 'success', 'message': 'Loan Request has been Approved'}
        return JsonResponse(data)
    
def decline_loan(request):
    if request.method == 'POST':
        loan_id = request.POST.get('loanId')
        obj_loan_table = loan_table.objects.get(loan_id=loan_id)
        obj_loan_table.is_approved = True
        obj_loan_table.save()
        data = {'status': 'success', 'message': 'Loan Declined'}
        return JsonResponse(data) 

def approve_payment(request):
    if request.method == 'POST':
        payment_request_number = request.POST.get('paymentRequestNumber')
        payment_request_obj = payment_request.objects.get(request_number=payment_request_number)
        request_dates = payment_request_obj.dates_request
        list_request_dates = eval(request_dates)
        loan_id = payment_request_obj.loan_id
        auditor = payment_request_obj.staff_name
        for request_date in list_request_dates:
            loan_payment_obj = loan_payment.objects.get(loan_id__loan_id=loan_id, dates_to_pay=request_date)
            loan_payment_obj.isAudit = True
            loan_payment_obj.paid = True
            loan_payment_obj.staff = auditor
            loan_payment_obj.save()
            payment_request_obj.is_approved = True
            payment_request_obj.save()
        loan_table_obj = get_object_or_404(loan_table, loan_id=loan_id)
        amount = payment_request_obj.amount
        loan_table_obj.paid_amount = loan_table_obj.paid_amount + int(amount)
        loan_table_obj.amount_left = loan_table_obj.amount_left - int(amount)
        loan_table_obj.paid_days = loan_table_obj.paid_days + len(list_request_dates)
        loan_table_obj.days_left = loan_table_obj.days_left - len(list_request_dates)
        loan_table_obj.save()
        
        data = {'status': 'success', 'message': 'Payment Audited'}
        return JsonResponse(data)