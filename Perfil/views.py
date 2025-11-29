from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from Perfil.serializers import CreatedRecipeSerializer
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

@login_required
def receta_detalle_view(request, pk):
    return render(request, "Perfil/receta-detalle.html", {"receta_id": pk})

def receta_detalle_api(request, pk):
    receta = get_object_or_404(RecetaCreada, pk=pk)
    serializer = CreatedRecipeSerializer(receta)
    return JsonResponse(serializer.data, safe=False)

@login_required
def editar_receta_view(request,pk):
    form = crearRecetaForm()
    return render(request, "Perfil/actualizarReceta.html", { "receta_id": pk, "form": form })
    