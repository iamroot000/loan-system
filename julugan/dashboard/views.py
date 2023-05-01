from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from loanmanager.models import bank, loan_table, borrower_table

# Create your views here.
class IndexView(View):

    def get(self, request):

        template = "dashboard/index.html"
        bank_obj = bank.objects.get(name="ACCOUNT1")
        active_loans = loan_table.objects.filter(is_active=True).count
        active_borrowers = borrower_table.objects.exclude(active_loans=0).count
        print(bank_obj.available_balance)
        context = {
            "active_loans": active_loans,
            "active_borrowers": active_borrowers,
            "available_balance": bank_obj.available_balance,
        }
        return render(request, template, context)