print("""
  _    _   ______
 | |  | | |  ____|     /\
 | |  | | | |__       /  \
 | |  | | |  __|     / /\ \
 | |__| | | |____   / ____ \
  \____/  |______| /_/    \_\

""")

#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
informacion_personal = {
    "nombre": "John Cueva",
    "edad": 28,
    "ciudad": "Coca",
}
#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["Ciudad"] = "Quito"
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion"] = "Desarrolladro"

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" in informacion_personal:
    print("El telefono está en el diccionario.")
else:
    informacion_personal["telefono"] = "099-679-4034"

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["edad"]

#Imprime el diccionario resultante después de realizar todas las operaciones.
print(informacion_personal)