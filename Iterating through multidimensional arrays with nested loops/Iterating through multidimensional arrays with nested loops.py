# Definimos la matriz 3D de temperaturas.
# Dimensiones: [Número de ciudades][Días de la semana][Número de semanas]
temperaturas = [
    # Ciudad 1
    [
        [22, 24, 21, 23, 20, 19, 25],  # Semana 1
        [24, 22, 26, 23, 27, 28, 21],  # Semana 2
        [20, 21, 19, 22, 24, 23, 22],  # Semana 3
    ],
    # Ciudad 2
    [
        [18, 19, 20, 21, 22, 23, 24],  # Semana 1
        [17, 16, 18, 20, 21, 19, 20],  # Semana 2
        [25, 24, 23, 22, 21, 20, 19],  # Semana 3
    ],
    # Ciudad 3
    [
        [30, 29, 31, 32, 33, 28, 27],  # Semana 1
        [34, 33, 35, 36, 32, 31, 30],  # Semana 2
        [28, 27, 26, 29, 30, 31, 32],  # Semana 3
    ]
]

# Nombres de las ciudades para referencia.
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Calculamos el promedio de temperaturas para cada ciudad por semana.
for i in range(len(ciudades)):  # Recorremos las ciudades usando su índice.
    print(f"Promedio de temperaturas para {ciudades[i]}:")
    for semana in range(len(temperaturas[i])):  # Recorremos las semanas de cada ciudad.
        suma_temperaturas = 0
        for dia in range(len(temperaturas[i][semana])):  # Recorremos los días de la semana.
            suma_temperaturas += temperaturas[i][semana][dia]
        # Calculamos el promedio para la semana actual
        promedio = suma_temperaturas / len(temperaturas[i][semana])
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()