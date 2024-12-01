#Ejercicio 5 
numeros = []
for i in range(10):
    numero = int(input("Ingrese 1 número: "))
    numeros.append(numero)
    if i == 0:
        numero_maximo = numero
    elif numero > numero_maximo:
        numero_maximo = numero
print(numeros)
print(f"El número más alto fue {numero_maximo}.")
