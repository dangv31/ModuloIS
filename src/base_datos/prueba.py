import sqlite3

conn = sqlite3.connect("prueba.db")

c = conn.cursor()
#Crear tabla
#c.execute("""CREATE TABLE estudiantes(
#                nombre TEXT,
#                edad INTEGER,
#                estatura REAL
#)""")
#Agregar un dato a la tabla
#c.execute("INSERT INTO estudiantes VALUES ('mark', 27, 1.90)")
#todos_estudiantes = [
#    ('Juan', 30, 1.80),
#    ('Pepe', 20, 1.60),
#    ('Messi', 80, 1.70),
#    ('Cr7', 40, 1.90)
#]
#Agregar varios datos a la tabla
#c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", todos_estudiantes)
#Abrir los datos de la tabla
c.execute("SELECT * FROM estudiantes")
lista = c.fetchall()
print(lista)
conn.commit()
conn.close()

