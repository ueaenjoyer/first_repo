def bubble_sort_row(matrix, row_number):
    # Verificar si el número de fila es válido
    if row_number < 0 or row_number >= len(matrix):
        raise ValueError("El número de fila está fuera del rango de la matriz")

    # Obtener la fila especificada
    row = matrix[row_number]

    # Implementar el algoritmo de bubble sort para ordenar la fila
    n = len(row)
    for i in range(n):
        for j in range(0, n - i - 1):
            if row[j] > row[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                row[j], row[j + 1] = row[j + 1], row[j]

    # Asignar la fila ordenada de nuevo a la matriz
    matrix[row_number] = row


print("\n\n---------------------------------------------------------------------\n")
print("This is a script for order a row.\n"
      "In order to work properly, you must pass 2 parameters:\n"
      "* The first is the matrix in which you want to order.\n"
      "* The second is the number you want to find.\n")

matriz = [
    [34, 2, 23, 7],
    [9, 14, 3, 0],
    [12, 5, 6, 1]
]

print("Matrix before bubble sort:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1) de la matriz
bubble_sort_row(matriz, 1)

print("\nMatrix after bubble sort in 2 row:")
for fila in matriz:
    print(fila)
