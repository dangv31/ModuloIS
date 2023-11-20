import pickle
import sqlite3
import os

from src.gestor_aplicacion.Categoria import Categoria


class Gestor_Base:
    @classmethod
    def guardar_maestro(cls, maestro):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        maestro = pickle.dumps(maestro)
        c.execute("INSERT INTO maestros (Maestro) VALUES (?)", (maestro,))
        conn.commit()
        conn.close()
    @classmethod
    def buscar_maestro(cls, nombre):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        c.execute("SELECT * FROM maestros")
        lista_maestros = c.fetchall()
        for ID, maestro in lista_maestros:
            maestro = pickle.loads(maestro)
            if maestro.nombre == nombre:
                return ID, maestro
        return None
    @classmethod
    def actualizar_maestro(cls, maestro, id):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        maestro = pickle.dumps(maestro)
        c.execute("UPDATE maestros SET Maestro = ? WHERE ID = ?", (maestro, id))
        conn.commit()
        conn.close()
    @classmethod
    def lista_maestros(cls):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        c.execute("SELECT * FROM maestros")
        lista_maestros = c.fetchall()
        maestros_deserializados = []
        for ID, maestro in lista_maestros:
            maestros_deserializados.append((ID, pickle.loads(maestro)))
        return maestros_deserializados
