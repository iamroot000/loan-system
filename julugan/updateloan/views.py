from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from loanmanager.models import loan_table

# Create your views here.
class IndexView(View):

    def get(self, request):

        template = "updateloan/index.html"

        getLoanTableDetails = loan_table.objects.filter(is_approved=True)
        context = {
            'getLoanTableDetails': getLoanTableDetails,
        }
        return render(request, template, context)