from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomRegisterForm, CustomLoginForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomRegisterForm()

    return render(request, 'perfil/auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomLoginForm()

    return render(request, 'perfil/auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

