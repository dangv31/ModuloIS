import sqlite3 as sq
import os


def crear_tabla_maestro(nombre, columnas):
    # Obtener la ruta al directorio del script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta al archivo de base de datos
    ruta_base_datos = os.path.join(directorio_script, 'maestros.db')
    conn = sq.connect(ruta_base_datos)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {nombre}({', '.join(columnas)})")
    conn.commit()
    conn.close()

