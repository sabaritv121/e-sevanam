from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_govt:
                return redirect('cmp_gov')
            elif user.is_user:
                return redirect('user_home')
        else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'Modified_files/login.html')

@login_required(login_url='login_view')
def index(request):
    return render(request, 'Modified_files/admin.html')

@login_required(login_url='login_view')
def user(request):
    return render(request,'user_home.html')


# def table(request):
#     return render(request, 'table.html')

@login_required(login_url='login_view')
def gov(request):
    return render(request, 'Modified_files/gov.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')