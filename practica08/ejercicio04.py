import csv

def ingresar_videojuegos():
    videojuegos = []
    n = int(input("¿Cuántos videojuegos deseas ingresar? "))
    
    for i in range(n):
        print(f"\nIngresando datos para el videojuego {i+1}:")
        nombre = input("Nombre del videojuego: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB (Ejemplo: E, T, M): ")
        
        videojuegos.append((nombre, genero, desarrollador, clasificacion))
    
    return videojuegos

def guardar_en_csv(videojuegos, archivo_salida):
    with open(archivo_salida, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter='\t')
        
        escritor_csv.writerow(['nombre', 'genero', 'desarrollador', 'clasificacion'])
        
        for videojuego in videojuegos:
            escritor_csv.writerow(videojuego)

    print(f"\nLos datos han sido guardados en '{archivo_salida}'.")

archivo_salida = 'videojuegos.csv' 
videojuegos = ingresar_videojuegos()

guardar_en_csv(videojuegos, archivo_salida)