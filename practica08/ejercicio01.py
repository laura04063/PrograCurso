def ordenar_canciones(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as entrada:
            canciones = entrada.readlines()

        canciones_limpias = []
        for cancion in canciones:
            cancion_limpia = ""
            for caracter in cancion:
                if caracter not in ['\n', '\t', ' ']:
                    cancion_limpia += caracter
            canciones_limpias.append(cancion_limpia)

        n = len(canciones_limpias)
        for i in range(n):
            for j in range(0, n-i-1):
                if canciones_limpias[j] > canciones_limpias[j+1]:
                    canciones_limpias[j], canciones_limpias[j+1] = canciones_limpias[j+1], canciones_limpias[j]

        with open(archivo_salida, 'w') as salida:
            for cancion in canciones_limpias:
                salida.write(cancion + '\n')

        print(f"Las canciones han sido ordenadas y guardadas en '{archivo_salida}'.")
    
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo_entrada = 'canciones.txt'
archivo_salida = 'canciones_ordenadas.txt'
ordenar_canciones(archivo_entrada, archivo_salida)