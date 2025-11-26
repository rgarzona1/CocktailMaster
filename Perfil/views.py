from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import RecetaCreada, RecetaGuardada, User, UserProfile
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from .forms import CustomRegisterForm, CustomLoginForm, crearRecetaForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/perfil/dashboard/')
    else:
        form = CustomRegisterForm()

    return render(request, 'Perfil/auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomLoginForm()

    return render(request, 'Perfil/auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def perfil_dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'Perfil/perfilUsuario.html', {
        'profile': profile
    })
    
@login_required
def crear_receta(request):
    form = crearRecetaForm()
    return render(request, "Perfil/crearReceta.html", {"form": form})
