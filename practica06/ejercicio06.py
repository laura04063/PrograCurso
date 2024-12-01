#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    #1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    #2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def ordenar_palabras(cadena):
    lista_palabras = []
    palabra = ""
 
    for caracter in cadena:
        if caracter == '-':
            lista_palabras.append(palabra)
            palabra = ""
        else:
            palabra += caracter
    lista_palabras.append(palabra)

    lista_ordenada = []
    
    while lista_palabras:
        menor_palabra = lista_palabras[0]
        for palabra in lista_palabras:
            if palabra < menor_palabra:
                menor_palabra = palabra
        lista_ordenada.append(menor_palabra)
        lista_palabras.remove(menor_palabra)

    cadena_ordenada = ""
    for i in range(len(lista_ordenada)):
        cadena_ordenada += lista_ordenada[i]
        if i < len(lista_ordenada) - 1:
            cadena_ordenada += '-'
    
    return cadena_ordenada

texto1 = "python-variable-funcion-computadora-monitor"
texto2 = "computadora-funcion-monitor-python-variable"
resultado1 = ordenar_palabras(texto1)
resultado2 = ordenar_palabras(texto2)
print(resultado1) 
print(resultado2)