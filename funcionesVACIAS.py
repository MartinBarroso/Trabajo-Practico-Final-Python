from configuracion import *
from principal import *
import math
import random

def DondeEsta(lista,elemento):
    for j in range (len(lista)): #recorro la lista con el len
        if lista[j]==elemento: #busco si el elemento esta en la lista
            return j #devuelve el indice, y si no esta devuelve -1

    return -1

def unaAlAzar(lista):
    elemento = random.choice(lista)
    return elemento

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    pos = items.index(item)
    if palabraUsuario[0]==letra and palabraUsuario in listaDeTodo[pos]:
        return 10
    else:
        return -5

def JuegaCompu(letraAzar, listaDeTodo):
    salida=[]
    for item in listaDeTodo:
        lista = []
        for palabra in item:
            if palabra[0]==letraAzar:
                lista.append(palabra)

        if len(lista)>0:
            salida.append(unaAlAzar(lista))

        else:
            salida.append(" ")

    print (salida)
    return salida


def leoLista(nombre):
    archivo = open (nombre+".txt","r")
    lista=[]
    for linea in archivo.readlines():
        lista.append(linea[:-1])
    archivo.close()
    return lista