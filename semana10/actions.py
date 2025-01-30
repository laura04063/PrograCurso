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
            print(estudiante)
    else:
        print("No hay estudiantes disponibles.")


def ver_mejores_estudiantes():
    if estudiantes:
        promedios = []
        for estudiante in estudiantes:
            suma_notas = sum(estudiante["notas"][materia] for materia in estudiante.notas)
            promedio = suma_notas / len(estudiante.notas)
            promedios.append((estudiante, promedio))

        mejores_estudiantes = []
        for _ in range(3):
            if promedios:
                max_estudiante = promedios[0]
                for estudiante, promedio in promedios:
                    if promedio > max_estudiante[1]:
                        max_estudiante = (estudiante, promedio)
                mejores_estudiantes.append(max_estudiante)
                promedios.remove(max_estudiante)

        print("\nTop 3 estudiantes con mejor promedio:")
        posicion = 1
        for estudiante, promedio in mejores_estudiantes:
            print(f"{posicion}. {estudiante['nombre']} - Promedio: {promedio:.2f}")
            posicion += 1
    else:
        print("No hay estudiantes disponibles.")


def ver_promedio():
    if estudiantes:
        promedios_individuales = []
        for estudiante in estudiantes:
            suma_notas = sum(estudiante["notas"][materia] for materia in estudiante.notas)
            promedio = suma_notas / len(estudiante["notas"])
            promedios_individuales.append(promedio)
        suma_promedios = sum(promedios_individuales)
        promedio_general = suma_promedios / len(promedios_individuales)
        print(f"\nPromedio General de Todos los Estudiantes: {promedio_general:.2f}")
    else:
        print("No hay estudiantes disponibles.")