from configuracion import *
from principal import *
import math
import random

def dondeEsta(lista,elemento):
    for j in range (len(lista)): #recorro la lista con el len
        if lista[j]==elemento: #busco si el elemento esta en la lista
            return j #devuelve el indice, y si no esta devuelve -1

    return -1

def unaAlAzar(lista):
    elemento = random.choice(lista) #Busca un elemento aleatorio de la lista
    return elemento


def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    if len(palabraUsuario)>0: #si el usuario toca solo enter le va a restar 5 puntos
        pal = items.index(item) #Toma el indice del item en la lista de items
        if palabraUsuario[0]==letra and palabraUsuario in listaDeTodo[pal]: #Si la palabraUsuario cumple con la condicion de la primer letra y esta en listaDeTodo, devuelve el puntaje
            return 10 
        else:
            return -5
    else:
        return -5
    

    def juegaCompu(letraAzar, listaDeTodo):
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


def leoLista (nombre): #Funcion LeoLista que pasaron los profes
    f = open(nombre+".txt", "r")
    lista=[]
    lineas=int(f.readline())
    for i in range(lineas):
        linea=f.readline()
        numeros.append(int(linea))
    f.close()
    
    return lista
