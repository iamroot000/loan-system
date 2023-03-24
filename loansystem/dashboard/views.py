from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from loan.models import loan_table

# Create your views here.
class index(View):

    def get(self, request):

        template = "dashboard/index.html"

        # loanTableDetails = loan_table.objects.filter(loanType="daily")
        # # loanTableDetails = loan_table.objects.all()
        # print(loanTableDetails)

        # context = {
        #     'loanTableDetails': loanTableDetails,
        # }

        return render(request, template)

def get_daily_table(request):

    loanTableDetails = loan_table.objects.filter(loan_type="daily")
    data = list(loanTableDetails.values())
    print(data)

    return JsonResponse({'data': data})