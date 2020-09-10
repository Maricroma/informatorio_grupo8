from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

    
def inicio(request):

    return render(request, 'index.html')

@login_required
def usuario(request):
     # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "registration/welcome.html")
    # En otro caso redireccionamos 
    return render(request, "registration/welcome.html")
