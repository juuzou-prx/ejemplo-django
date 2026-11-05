from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Perfil

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('lista_libros')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            Perfil.objects.get_or_create(user=user)
            login(request, user)
            return redirect('lista_libros')
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'registro/iniciar_sesion.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro/registrar_usuario.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')