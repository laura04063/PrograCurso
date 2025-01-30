import actions
import data

def mostrar_menu():
    while True:
        print("\nMenu:")
        print("1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Ver top 3 de estudiantes con mejor promedio")
        print("4. Ver nota promedio de todos los estudiantes")
        print("5. Exportar datos a un archivo CSV")
        print("6. Importar datos desde un archivo CSV")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            actions.agregar_estudiante()
        elif opcion == "2":
            actions.ver_estudiantes()
        elif opcion == "3":
            actions.ver_mejores_estudiantes()
        elif opcion == "4":
            actions.ver_promedio()
        elif opcion == "5":
            data.exportar_datos()
        elif opcion == "6":
            data.importar_datos()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")