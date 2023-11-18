from src.gestor_aplicacion.Maestro import Maestro


def buscar_maestro(nombre):
    for i in range(len(Maestro.lista_maestros)):
        if Maestro.lista_maestros[i].nombre == nombre:
            return Maestro.lista_maestros[i]
        else:
            return False
