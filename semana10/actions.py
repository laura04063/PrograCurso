import student

estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre completo: ")
    seccion = input("Ingrese la sección: ")
    notas = {}

    for materia in ["Español", "Inglés", "Sociales", "Ciencias"]:
        while True:
            try:
                nota = float(input(f"Ingrese la nota de {materia}: "))
                if 0 <= nota <= 100:
                    notas[materia] = nota
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida, ingrese un número.")

    estudiante = student.Student(nombre, seccion, notas)
    estudiantes.append(estudiante)
    print("Estudiante agregado exitosamente.")

def ver_estudiantes():
    if estudiantes:
        for estudiante in estudiantes:
            print("\nNombre:", estudiante.nombre)
            print("Sección:", estudiante.seccion)
            for materia, nota in estudiante.notas.items():
                print(f"Nota de {materia}: {nota}")
    else:
        print("No hay estudiantes disponibles.")

def ver_mejores_estudiantes():
    if estudiantes:
        promedios = [(estudiante, estudiante.calcular_promedio()) for estudiante in estudiantes]
        mejores_estudiantes = sorted(promedios, key=lambda x: x[1], reverse=True)[:3]

        print("\nTop 3 mejores estudiantes:")
        for estudiante, promedio in mejores_estudiantes:
            print(f"{estudiante.nombre} - Promedio: {promedio:.2f}")
    else:
        print("No hay estudiantes registrados.")

def ver_promedio():
    if estudiantes:
        promedios_individuales = [estudiante.calcular_promedio() for estudiante in estudiantes]
        promedio_general = sum(promedios_individuales) / len(promedios_individuales)
        print(f"\nNota promedio general: {promedio_general:.2f}")
    else:
        print("No hay estudiantes registrados.")