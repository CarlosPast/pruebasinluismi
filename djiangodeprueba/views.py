from django.shortcuts import render, redirect
from .models import *
from .añadir_datos import *
# Create your views here.
def cargar_pagina_inicio(request):

    return render(request,'inicio.html')

def registroDatos(request):
    lista_datos = prueba.objects.all()
    lista_datos2 = prueba_del_algodon.objects.all()

    if request.method == "GET":

        return render(request,'ListaPrueba.html',{'prueba': lista_datos,"prueba_algodon":lista_datos2})
    else :
        nuevo_user = Usuario()
        nuevo_user.username = request.POST.get("name")
        nuevo_user.password = request.POST.get("pass")
        Usuario.save(nuevo_user)
        return redirect('/djiangodeprueba/prueba')

