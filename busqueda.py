matriz = [
    [15, 25, 20],
    [30, 40, 35],
    [50, 45, 55]
]

valor_buscado = 50

fila_encontrada = -1

columna_encontrada = -1

for fila in range(len(matriz)):
    for columna in range(len(matriz)):

        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna

            break

    if fila_encontrada != -1:
        break

if fila_encontrada != -1:
    print(f"se encontro {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"{valor_buscado} no se encontro en la matriz.")