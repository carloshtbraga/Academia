from django.shortcuts import render
from .forms import Formulario
from .models import Academia


def home(request):
    form = Formulario()
    return render(request, "smartfit/home.html", {"form": form})


def processa_formulario(request):
    form = Formulario(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return render(request, "smartfit/processa_formulario.html")


def lista_academias(request):
    academias = Academia.objects.all()
    return render(request, "smartfit/lista_academias.html",  context = {'academias': academias})