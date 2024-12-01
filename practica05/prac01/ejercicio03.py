#Ejercicio 3
elementos = ["estas", "como", "Hola,"]

if len(elementos) > 1:
    primer_elemento = elementos[0]
    ultimo_elemento = elementos[-1]
    elementos[0] = ultimo_elemento
    elementos[-1] = primer_elemento
print(elementos)