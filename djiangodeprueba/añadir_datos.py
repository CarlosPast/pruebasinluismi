from .models import *

def cargar_datos():
    new_prueba_del_algodon = prueba_del_algodon()
    new_prueba_del_algodon.nombre = "Zacarias"
    new_prueba_del_algodon.apellidos = "Payaso"
    prueba_del_algodon.save(new_prueba_del_algodon)

