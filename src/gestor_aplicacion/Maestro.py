import sqlite3 as sq
class Maestro:
    lista_maestros = []
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.columnas = columnas
        self.categorias = []
        self.observaciones = []
        self.estado = True


