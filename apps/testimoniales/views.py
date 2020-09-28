# Create your views here.
from django.shortcuts import render

def Testimonial(request):
    return render(request, 'testimoniales/testimonial.html')