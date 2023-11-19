from src.gestor_aplicacion.Maestro import Maestro


def buscar_maestro(nombre):
    for maestro in Maestro.lista_maestros:
        if maestro.nombre == nombre:
            return maestro
    return None