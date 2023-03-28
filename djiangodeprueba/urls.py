from django.contrib import admin
from django.urls import path, include
from .views import *
import djiangodeprueba

urlpatterns = [
    path('', cargar_pagina_inicio),
    path('prueba/', registroDatos)
]