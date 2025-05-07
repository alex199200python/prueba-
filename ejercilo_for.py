

suma_notas = 0


for i in range(1, 4):
    nota = float(input(f"Ingrese la nota {i}: "))
    suma_notas += nota


promedio = suma_notas / 3


print(f"El promedio de las 3 notas es: {promedio:.2f}")
