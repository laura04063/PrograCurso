#Ejercicio 1 
informacion = {
	"Nombre" : "Resort Guanacaste",
	"Numero de estrellas" : 5,
	"Habitaciones1" : [
        {"numero": 1,
         "Piso" : 2,
         "Precio por noche": 100000}, 

        {"numero": 1,
         "Piso" : 2,
         "Precio por noche": 100000}
        ]
}

for variables, info in informacion.items():
  print(f'{variables} : {info}')