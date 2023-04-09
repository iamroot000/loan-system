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
        #display currently logged in user
        #print(request.user.username)

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
