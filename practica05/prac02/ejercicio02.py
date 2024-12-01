#Ejercicio 2
diccionario = {}
keys = ["Nombre: ", "Apellido: ", "Direccion: "]
values = ["Cristobal", "Angulo", "Moravia"]

for index in range(len(keys)):
        diccionario[keys[index]] = values[index]
        print(diccionario)