from src.gestor_aplicacion.Sede import Sede


def buscar_sede():
    nombre_sede = input("Ingrese el nombre de la sede: ")
    for sede in Sede.lista_sedes:
        if sede.nombre == nombre_sede:
            return sede
    return None