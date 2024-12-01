import csv
import actions

def exportar_datos():
    if actions.estudiantes:
        with open("datos_estudiantes.csv", mode="w", newline="") as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias"])

            for estudiante in actions.estudiantes:
                escritor.writerow([
                    estudiante["nombre"],
                    estudiante["seccion"],
                    estudiante["notas"]["Español"],
                    estudiante["notas"]["Inglés"],
                    estudiante["notas"]["Sociales"],
                    estudiante["notas"]["Ciencias"]
                ])
        print("Datos exportados exitosamente a datos_estudiantes.csv.")
    else:
        print("No hay datos para exportar.")

def importar_datos():
    try:
        with open("datos_estudiantes.csv", mode="r") as file:
            lector = csv.DictReader(file)
            for fila in lector:
                estudiante = {
                    "nombre": fila["Nombre"],
                    "seccion": fila["Sección"],
                    "notas": {
                        "Español": float(fila["Español"]),
                        "Inglés": float(fila["Inglés"]),
                        "Sociales": float(fila["Sociales"]),
                        "Ciencias": float(fila["Ciencias"])
                    }
                }
                actions.estudiantes.append(estudiante)
        print("Datos importados exitosamente.")
    except FileNotFoundError:
        print("No se encontró un archivo de datos exportado previamente.")