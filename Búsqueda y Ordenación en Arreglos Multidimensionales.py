#Programación en Python y Sincronización con GitHub - Búsqueda y Ordenación en Arreglos Multidimensionales

matrix = [
    [2, 4, 8, 6],
    [3, 9, 4, 7],
    [1, 6, 3, 8]
]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sort_row(matrix, row_index):
    row = matrix[row_index]

    bubble_sort(row)

    matrix[row_index] = row


print("Matriz original:")
for row in matrix:
    print(row)

sort_row(matrix,1)

print("\nMatriz después de ordenar la fila 1:")
for row in matrix:
    print(row)