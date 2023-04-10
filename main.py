'''
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
'''

import sqlite3

conn = sqlite3.connect('.alumno.db')

cursor = conn.cursor()


consulta = cursor.execute('SELECT * FROM alumnos WHERE name= "jimmy"')



for row in consulta:
    print(row)



cursor.close()

conn.close()
