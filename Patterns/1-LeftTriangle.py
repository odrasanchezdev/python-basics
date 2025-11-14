# Pide al usuario cuantas líneas tendra el triangulo.
rows = int(input("Number of lines: "))

# Recorre cada fila del triangulo.
for i in range(0, rows):
    # En cada fila, imprime tantos asteriscos como el numero de fila actual.
    for j in range(0, i + 1):
        print("*", end=' ')
    
    # Despues de terminar la fila, hace un salto de línea.
    print("\r")
