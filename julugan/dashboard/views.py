from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):

    def get(self, request):

        template = "dashboard/index.html"

        return render(request, template)