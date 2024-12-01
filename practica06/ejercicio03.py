# Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41

lista=[4,6,2,29]
def suma_lista(lista):
    suma = 0 
    for listas in lista:
        suma += listas 
    return suma

sumas = suma_lista(lista)
print (sumas)