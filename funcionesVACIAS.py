from configuracion import *
from principal import *
import math
import random

#Toma un elemento aleatorio de la lista y devuelve el elemento
def unaAlAzar(lista):
    elemento = random.choice(lista)
    return elemento

#Chequea si la palabra es correcta o no y le asigna un puntaje
def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    if len(palabraUsuario)>0:

#Toma el indice del item en la lista de items
       posicion = items.index(item)

#Si la palabraUsuario cumple con la condicion de la primer letra y esta en listaDeTodo
#Devuelve puntaje positivo. De lo contrario negativo
       if palabraUsuario[0]==letra and palabraUsuario in listaDeTodo[posicion]:
            return 10
       else:
            return -5
    else:
        return -5


#Hace que la PC elija palabras para jugar con el jugador
def juegaCompu(letraAzar, listaDeTodo):
    salida=[]

#Recorre la lista de todas las palabras y luego la lista de item
    for item in listaDeTodo:
        lista = []

        for palabra in item:

#Agrega a "lista" la palabra que empiece con la misma letra inicial
            if palabra[0]==letraAzar:
                lista.append(palabra)

#Agrega a la lista "salida" el elemento agregado a "lista"
        if len(lista)>0:vb
            salida.append(unaAlAzar(lista))

        else:
            salida.append(" ")

#devuelve el elemento en "salida"
    return salida


#Funcion que nos permite abrir distintos archivos de texto y leerlos
#Nos permite agregar mas palabras y categorias al juego
def LeoLista(archivo_txt):
    stop_words=open(archivo_txt,'r')
    lineas = [linea.split() for linea in stop_words]
    total=list()

    for linea in lineas:
        total+=linea

    return total
