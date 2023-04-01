from django.shortcuts import redirect, render
from django.views import View

# Create your views here.

class ManageSystem(View):

    def get(self, request):
        template = 'loan/index.html'
        return render(request, template)