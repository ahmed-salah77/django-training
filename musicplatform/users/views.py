from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View

class LoginView(View):
    def login(request):
        if(request.method == 'POST'):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('artists')
            else:
                messages.success(request,("username and password do not match"))
                return redirect('login')
        else:
            return render(request,'authenticate/login.html',{})
        

