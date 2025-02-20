import csv
import actions
import student

def exportar_datos():
    if actions.estudiantes:
        with open("datos_estudiantes.csv", mode="w", newline="") as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias"])

            for estudiante in actions.estudiantes:
                escritor.writerow([
                    estudiante.nombre,
                    estudiante.seccion,
                    estudiante.notas.get("Español", 0),
                    estudiante.notas.get("Inglés", 0),
                    estudiante.notas.get("Sociales", 0),
                    estudiante.notas.get("Ciencias", 0)
                ])

        print("Datos exportados exitosamente a datos_estudiantes.csv.")
    else:
        print("No hay datos para exportar.")

def importar_datos():
    try:
        with open("datos_estudiantes.csv", mode="r") as file:
            lector = csv.DictReader(file)
            for fila in lector:
                estudiante = student.convertirDesdeDiccionario(fila)  # Aquí usamos la función
                actions.estudiantes.append(estudiante)
        print("Datos importados exitosamente.")
    except FileNotFoundError:
        print("No se encontró el archivo.")