#ejercicio 3
list_keys = ["Direccion", "Edad"]
diccionario2 = {"nombre": "Maria", "Apellido": "Lopez", "Direccion": "Coronado", "Edad": 19}

for key in list_keys:
    diccionario2.pop(key) 
print(diccionario2)