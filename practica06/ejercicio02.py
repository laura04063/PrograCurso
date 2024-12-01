# Experimente con el concepto de scope:
    #1. Intente accesar a una variable definida dentro de una función desde afuera.
def variable_definida():
    lista= [1,2,3,4,5,6,7]
    print (lista)
    
variable_definida()


    #2.  Intente accesar a una variable global desde una función y cambiar su valor.
lista=[1,2,3,4,5,6,7]
def cambiar_lista():
    lista.append(8)
    print (lista)

cambiar_lista()