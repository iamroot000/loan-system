from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class index(View):

    def get(self, request):
        template = "login/index.html"
        return render(request, template)

    def post(self, request):
        template = "dashboard/index.html"
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
    
        authUser = authenticate(request, username=getUsername, password=getPassword)

        if authUser is not None:
            login(request, authUser)
            return redirect('dashboard:dashboard')
