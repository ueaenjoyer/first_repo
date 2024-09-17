print("***  \n   Deber de programación semana 14")
print("   Parámetro y retorno de variables en funciones")


# Definir la función para calcular descuento
def calcular(valor, descuento=15):
    """
    Calcula el descuento aplicado a un valor dado.

    :param valor: El valor original sobre el cual se calcula el descuento.
    :param descuento: El porcentaje de descuento a aplicar (por defecto es 15%).
    :return: El monto del descuento.
    """
    resultado = (valor * descuento) / 100
    return resultado


# Función para imprimir "UEA" en arte ASCII
def uea():
    """
    Imprime "UEA" en arte ASCII.
    """
    print("""
##  ###  ### ###    ##     
##   ##   ##  ##     ##    
##   ##   ##       ## ##   
##   ##   ## ##    ##  ##  
##   ##   ##       ## ###  
##   ##   ##  ##   ##  ##  
 ## ##   ### ###   ###  ##  
""")


# Llamar a la función para imprimir "UEA"
uea()

# Bucle principal del menú
while True:
    print("\nScript para calcular el descuento de una compra, por defecto se calcula el 15% de descuento")

    # Bucle para validar que se ingrese solo un número para el valor de la compra
    while True:
        try:
            valorUsuario = float(input("Ingrese el valor de la compra\nOjo: Solo se admiten números\n"))
            break
        except ValueError:
            print("Ingrese un número válido\n")

    # Preguntar al usuario si desea calcular el descuento por defecto
    contol = input("Desea calcular el descuento por defecto? (15%) S/N\n").strip().lower()

    if contol in ["s", "si", "y", "yes"]:
        # Calcular y mostrar el descuento por defecto del 15%
        print(f"El %15 de descuento de {valorUsuario} es {calcular(valorUsuario)}")
    elif contol in ["n", "no"]:
        # Bucle para validar que se ingrese solo un número para el porcentaje de descuento
        while True:
            try:
                porcentajeUsu = float(
                    input("Ingrese el porcentaje de descuento que desea calcular\nOjo: Solo se admiten números\n"))
                break
            except ValueError:
                print("Ingrese un número válido\n")

        # Calcular y mostrar el descuento con el porcentaje ingresado por el usuario
        print(f"El {porcentajeUsu}% de descuento de {valorUsuario} es: {calcular(valorUsuario, porcentajeUsu)}")
    else:
        print("Selección no válida. Escriba 'si' o 'no' ")

    # Preguntar al usuario si desea realizar otro cálculo
    otra_vez = input("¿Desea realizar otro cálculo? (S/N)\n").strip().lower()
    if otra_vez not in ["si", "s", "y", "yes"]:
        print("Saliendo del programa...")
        break
