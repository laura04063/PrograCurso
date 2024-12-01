notas_aprobadas = 0
notas_desaprobadas = 0
suma_aprobadas = 0
suma_desaprobadas = 0
promedio_total = 0
cantidad_notas = int(input("Ingrese la cantidad de notas: "))

for i in range(cantidad_notas):
    nota = int(input(f"Ingrese la nota del estudiante {i + 1}: "))
    if nota >= 70:
        notas_aprobadas += 1
        suma_aprobadas += nota
    else:
        notas_desaprobadas += 1
        suma_desaprobadas += nota

if notas_aprobadas > 0:
    promedio_aprobadas = suma_aprobadas / notas_aprobadas
else:
    promedio_aprobadas = 0

if notas_desaprobadas > 0:
    promedio_desaprobadas = suma_desaprobadas / notas_desaprobadas
else:
    promedio_desaprobadas = 0

promedio_total = (suma_aprobadas + suma_desaprobadas) / cantidad_notas
print("La cantidad de aprobadas son:", notas_aprobadas)
print("La cantidad de desaprobadas son:", notas_desaprobadas)
print("El promedio de aprobadas es:", promedio_aprobadas)
print("El promedio de desaprobadas es:", promedio_desaprobadas)
print("El promedio total es:", promedio_total)