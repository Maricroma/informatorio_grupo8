from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
# Create your views here.

    
def inicio(request):

    return render(request, 'index.html')
    

def historia(request):

    return render(request, 'historia.html')

