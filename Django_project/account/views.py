from django.shortcuts import render, redirect
from django.contrib.auth import login

from account.forms import RegistrationForm, LoginForm
from account.models import User


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return redirect('login')
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    return render(request, 'account/login.html', {'form': form})