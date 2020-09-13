from django.shortcuts import render

# Create your views here.


def participante(request):

    return render(request, 'usuarios/participante.html')