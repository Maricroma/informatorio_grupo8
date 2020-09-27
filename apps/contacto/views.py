from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto(request):
    template = 'contacto/contacto.html'

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect(to='inicio')
    else:
        form = ContactoForm()

    data = {
        'form': form,
    }

    return render(request, template, data)
