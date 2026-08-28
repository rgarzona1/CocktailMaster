from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme

from Perfil.serializers import CreatedRecipeSerializer
from .models import RecetaCreada, RecetaGuardada, User, UserProfile
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from .forms import CustomRegisterForm, CustomLoginForm, UserProfileForm, crearRecetaForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, avatar=form.cleaned_data.get('avatar'))
            login(request, user)
            return redirect('/perfil/dashboard/')
    else:
        form = CustomRegisterForm()

    return render(request, 'Perfil/auth/register.html', {'form': form})


def login_view(request):
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('perfil_dashboard')
    else:
        form = CustomLoginForm()

    return render(request, 'Perfil/auth/login.html', {
        'form': form,
        'next': next_url,
    })


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


@login_required
def editar_perfil(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil_dashboard') 
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'Perfil/editarPerfil.html', {'form': form})