def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Función que calcula la temperatura promedio para cada ciudad
    durante un período de tiempo determinado (múltiples semanas).

    Parámetros:
    - temperaturas: lista tridimensional que contiene los datos de temperatura.
                    La estructura es [Número de ciudades][Días de la semana][Número de semanas].
    - ciudades: lista con los nombres de las ciudades en el mismo orden que la matriz de temperaturas.

    Retorno:
    - Una lista con los promedios de temperatura para cada ciudad.
    """
    promedios_ciudades = []  # Lista para almacenar el promedio de cada ciudad

    # Recorremos cada ciudad por su índice
    for ciudad_index in range(len(ciudades)):
        suma_total = 0  # Variable para acumular la suma total de temperaturas de la ciudad
        total_dias = 0  # Variable para contar el número total de días

        # Recorremos las semanas de cada ciudad
        for semana in temperaturas[ciudad_index]:
            suma_total += sum(semana)  # Sumamos las temperaturas de todos los días en la semana
            total_dias += len(semana)  # Contamos el número de días de la semana

        # Calculamos el promedio de temperaturas de la ciudad
        promedio = suma_total / total_dias
        # Almacenamos el promedio en la lista
        promedios_ciudades.append(promedio)

    return promedios_ciudades  # Retornamos la lista con los promedios


# Datos de ejemplo
temperaturas = [
    # Ciudad 1
    [
        [22, 24, 21, 23, 20, 19, 25],  # Semana 1
        [24, 22, 26, 23, 27, 28, 21],  # Semana 2
        [20, 21, 19, 22, 24, 23, 22],  # Semana 3
        [23, 22, 25, 20, 21, 19, 22]  # Semana 4
    ],
    # Ciudad 2
    [
        [18, 19, 20, 21, 22, 23, 24],  # Semana 1
        [17, 16, 18, 20, 21, 19, 20],  # Semana 2
        [25, 24, 23, 22, 21, 20, 19],  # Semana 3
        [20, 19, 18, 17, 16, 15, 14]  # Semana 4
    ],
    # Ciudad 3
    [
        [30, 29, 31, 32, 33, 28, 27],  # Semana 1
        [34, 33, 35, 36, 32, 31, 30],  # Semana 2
        [28, 27, 26, 29, 30, 31, 32],  # Semana 3
        [31, 30, 29, 28, 27, 26, 25]  # Semana 4
    ]
]

ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamamos a la función para calcular los promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

# Mostramos los resultados
for i in range(len(ciudades)):
    print(f"Promedio de temperaturas en {ciudades[i]}: {promedios[i]:.2f}°C")
