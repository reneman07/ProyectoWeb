from django.shortcuts import render, HttpResponse
from django.conf import settings
from carro.views import Carro

# Create your views here.
def home(request):
    carro = Carro(request)
    return render(request, "ProyectoWebApp/home.html")

