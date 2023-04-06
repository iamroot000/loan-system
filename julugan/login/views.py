from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

class IndexView(View):
    
    def get(self, request):
        template = "login/index.html"
        return render(request, template)

    def post(self, request):
        print("WOOOOOOOOOOOOOAAAHHHHHH")
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")

    
        authUser = authenticate(request, username=getUsername, password=getPassword)

        if authUser is not None:
            login(request, authUser)
            context = {'data': '/', 'message': ''}
        else:
            context = {'data': '/login', 'message': 'Invalid username or password'}
        
        return JsonResponse({'context': context})

