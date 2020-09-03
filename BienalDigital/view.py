from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import CustomUserForm
from django.http import HttpResponseRedirect
# Create your views here.
def Home(request):
    return render(request, 'index.html')
    
@login_required
def welcome(request):
     # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "registration/welcome.html")
    # En otro caso redireccionamos 
    return render(request, "registration/welcome.html")

def register(request):
    data={
        'form':CustomUserForm()
    }
    if request.method=='POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('')
        else:
            print("Un error ocurrio, vuelva a intentar")
    return render(request, "registration/register.html", data)

