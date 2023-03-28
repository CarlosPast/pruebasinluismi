from django.shortcuts import render
from .models import *
from .añadir_datos import *
# Create your views here.
def cargar_pagina_inicio(request):

    return render(request,'inicio.html')

def registroDatos(request):
    lista_datos = prueba.objects.all()
    lista_datos2 = prueba_del_algodon.objects.all()
    return render(request,'ListaPrueba.html',{'prueba': lista_datos,"prueba_algodon":lista_datos2})