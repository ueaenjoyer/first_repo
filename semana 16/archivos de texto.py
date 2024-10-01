"""Tarea: Trabajo con Archivos de Texto en Python

En esta tarea, realizarás operaciones de lectura y escritura en archivos de texto en Python. Sigue las instrucciones detalladas a continuación:

Escritura de Archivo de Texto:

Crea un nuevo archivo llamado my_notes.txt.
Escribe al menos tres líneas de notas personales en el archivo.
Lectura de Archivo de Texto:

Abre el archivo my_notes.txt.
Lee el contenido del archivo línea por línea utilizando el método adecuado.
Muestra en la consola cada línea leída.
Cierre de Archivos:

Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
Instrucciones Adicionales:

Utiliza métodos como write() y readline() para manipular el archivo de texto.
Agrega comentarios explicativos en tu código.
Guarda tu código en un repositorio de GitHub que ya hayas creado anteriormente para esta asignatura.
Sube el link donde se encuentra el código fuente de esta tarea en tu repositorio GitHub
Recuerda que cualquier duda o dificultad, puedes contactarme para obtener asistencia. ¡Buena suerte!"""


#Crea un nuevo archivo llamado my_notes.txt.
notas = open('my_notes.txt', 'w')  #  Crea el archivo si no esta creado, abrir el archivo en modo escritura

#Escribe al menos tres líneas de notas personales en el archivo.
# Usar write() para agregar contenido linea por linea
notas.write('Nota 1: Mi banda favorita es TAME IMPALA.\n')
notas.write('Nota 2: La mejor cancion de TAME IMPALA es LET IT HAPPEN.\n')

# Usar writelines() para agregar múltiples líneas
texto_multilinea = [
    'Nota 3: TAmbien disfruto mucho el rock y el nu-metal.\n',
    'Nota 4: Aveces tambien suelo escuchar hiphop.\n',
    'Nota 5: Prefiero la musica en ingles, aunque en español me gustan las de rock antiguo.\n'
]
notas.writelines(texto_multilinea)  # Escribe varias líneas de una sola vez

# Cerrar el archivo
notas.close()

"""Lectura de Archivo de Texto:

Abre el archivo my_notes.txt.
Lee el contenido del archivo línea por línea utilizando el método adecuado.
Muestra en la consola cada línea leída."""

notas = open('my_notes.txt', 'r')
linea = notas.readline()  # Leer la primera línea
while linea:  # Mientras haya líneas que leer
    print(linea.strip())  # Mostrar la línea leída, quitando los espacios en blanco
    linea = notas.readline()  # Leer la siguiente línea

# Cerrar el archivo después de leer
notas.close()
