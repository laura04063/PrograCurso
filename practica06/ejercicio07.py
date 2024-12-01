#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    #1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    #2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    #3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def es_primo(numero):
    if numero < 2:
        return False
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True


def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos
lista = [1,4,6,7,13,9,67]
resultado = filtrar_primos(lista)
print(resultado)