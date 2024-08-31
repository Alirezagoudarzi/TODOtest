from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_user(request):
    
    if (request.method=="POST"):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['user'],cd['email'],cd['password'])
            messages.success(request,'user registration successfuly','success')
            return redirect('home')
    else:
        form=UserRegistrationForm()

    return render (request,'register.html',{'form':form})



def user_login(request):
    if (request.method=="POST"):
            form=UserLoginForm(request.POST)
            if form.is_valid():
                 cd=form.cleaned_data
                 user= authenticate(request,username=cd['user'],password=cd['password'])
                 if user is not None :
                      login(request,user)
                      messages.success(request,'user login successfully','success')
                      return redirect('home')
    else:
        form=UserLoginForm()
    return render(request,'login.html',{'form':form})



def user_logout(request):
     logout(request)
     messages.success(request,'user logout successfully','success')
     return redirect('home')