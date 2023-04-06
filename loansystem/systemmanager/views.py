from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse, HttpResponse
from loan.models import loan_table, borrower_table, loan_payment, payment_request

# Create your views here.

class ManageSystem(View):

    def get(self, request):
        template = 'adminmanager/index.html'

        loanTableDetails = loan_table.objects.filter(is_approved=False)
        # data = list(loanTableDetails.values())
        context = {
            'requested_loan_list': loanTableDetails
        }
        return render(request, template)

# def get_request_table(request):

    

#     return JsonResponse({'data': data})
    
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