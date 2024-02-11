from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User


#Local imports
from . import forms

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Realiza tus propias validaciones aquí si es necesario
        
        if password1 != password2:
            return render(request, 'users/register.html', {'error_message': 'Las contraseñas no coinciden'})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return redirect(reverse('users-profile'))
        except Exception as e:
            return render(request, 'users/register.html', {'error_message': 'Error al registrar el usuario, puede que el nombre de usuario ya esté en uso'})
    else:
        return render(request, 'users/register.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirigir a la página de inicio de sesión exitosa
            return redirect(reverse('users-profile'))
        else:
            # Mostrar un mensaje de error en el inicio de sesión
            return render(request, 'users/login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        return render(request, 'users/login.html')


@login_required() # No te deja entrar en la página si no estás logeado (y te redirige a LOGIN_URL)
def profile(request):
    if request.method == "POST":
        user = request.user
        web = request.POST.get('web')
        github = request.POST.get('github')
        twitter = request.POST.get('twitter')
        if web != "":
            user.web = web
            user.save()
            print("Si que es diferente", user.web)
        if github != "":
            user.github = github
            user.save()
            print("Si que es diferente", user.github)
        if twitter != "":
            user.twitter = twitter
            user.save()
            print("Si que es diferente", user.twitter)
        
            
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('users-login'))