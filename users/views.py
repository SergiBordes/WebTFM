from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Local imports
from . import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, tu cuenta ha sido creada!, por favor, inicia sesión.")
            return redirect('users-login')
    else:
        form  = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required() # No te deja entrar en la página si no estás logeado (y te redirige a LOGIN_URL)
def profile(request):
    return render(request, 'users/profile.html')