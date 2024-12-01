def menu():
    print("\nCalculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")

def calcular():
    numero_actual = 0
    while True:
        print(f"\nNúmero actual: {numero_actual}")
        menu()
        try:
            opcion = int(input("Selecciona una opción (1-6):"))
        except ValueError:
            print("Opción inválida, ingresa un número entre 1 y 6")
            continue
        if opcion == 1:
            try:
                nuevo_numero = float(input("Ingresa un número para sumar:"))
                numero_actual += nuevo_numero
            except ValueError:
                print("Número inválido")
        elif opcion == 2:
            try:
                nuevo_numero = float(input("Ingresa un número para restar:"))
                numero_actual -= nuevo_numero
            except ValueError:
                print("Número inválido")
        elif opcion == 3:
            try:
                nuevo_numero = float(input("Ingresa un número para multiplicar:"))
                numero_actual *= nuevo_numero
            except ValueError:
                print("Número inválido")
        elif opcion == 4:
            try:
                nuevo_numero = float(input("Ingresa un número para dividir:"))
                if nuevo_numero == 0:
                    print("No se puede dividir entre 0")
                else:
                    numero_actual /= nuevo_numero
            except ValueError:
                print("Número inválido")
        elif opcion == 5:
            numero_actual = 0
            print("El resultado ha sido borrado")
        elif opcion == 6:
            print("Gracias por usar la calculadora")
            break
        else:
            print("Opción inválida, selecciona una opción del 1 al 6")
            
calcular()