import sqlite3

#conexión a la base de datos (se creara si no existe)
conn=sqlite3.connect("prueba.db")

#Crea cursos para interactuar con la base de datos
cursor= conn.cursor()

#Crea una tabla llamada usuarios con tres columnas: id, nombre y edad
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER
               )''')

#Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()