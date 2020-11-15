from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.


def createUser_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        customer = Customer.objects.all()

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'customer': customer, 'form': form}
        return render(request, 'createuser.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Your Account Has Been Disabled')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)
