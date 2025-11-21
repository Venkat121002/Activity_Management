from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .forms import RegistrationForm,LoginForm
# Create your views here.
def registraion_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        template_name = 'users/registration.html'
        context = {'form':form}
        return render(request,template_name,context)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            obj = User(
                first_name=firstname,
                last_name=lastname,
                email=email,
                username=username,
                password=make_password(password),
            )

            obj.save()
            return redirect('login-page')
        
        else:
            template_name = 'users/registration.html'
            context = {'form':form}
            return render(request,template_name,context)

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        template_name = 'users/login.html'
        context = {'form':form}
        return render(request,template_name,context)
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)

            print("Authenicate user: ",user)
            if user is not None:
                login(request,user)
                return redirect('home')
            
            else:
                message = "Invalid Credientaials"
                template_name = 'users/login.html'
                context = {'form':form,'error':message}
                return render(request,template_name,context)
        
        else:
            template_name = 'users/login.html'
            context = {'form':form}
            return render(request,template_name,context)
        
def logout_view(request):
    logout(request)
    return redirect('login-page')