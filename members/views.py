from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('task_app:list_task'))
        else:
            messages.success(request,"There was an error Logging In ! Try Again ...")
            return redirect('/members/login_user/')
    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('members:login_user'))

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Registration Successful !")
            return redirect(reverse('task_app:list_task'))
    else:
        form = RegisterUserForm()
    return render(request,'authenticate/register_user.html',context={'form':form})