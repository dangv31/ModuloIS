import pickle
import sqlite3
import os
class Gestor_Base:
    @classmethod
    def guardar_maestro(cls, maestro):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()

        maestro = pickle.dumps(maestro)
        print(maestro)
        c.execute("INSERT INTO maestros (Maestro) VALUES (?)", (maestro,))
        conn.commit()
        conn.close()

