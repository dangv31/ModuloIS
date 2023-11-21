from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Maestro import Maestro


class Crear_Maestro:
    @classmethod
    def crear_maestro(cls, cuenta):
        i = 1
        columnas = []
        while True:
                nombre = input("Ingrese el nombre del maestro: ")
                busqueda = Gestor_Base.buscar_objeto(nombre, "Maestro")
                if busqueda is None:
                    break
                else:
                    print("Ya existe un maestro con ese nombre, ingrese otro nombre")
                    from src.ui_main.Menu_inicial import Menu_inicial
                    return Menu_inicial.menu_inicial_Administrativo(cuenta)
        print("Ingrese el nombre de las columnas, si no desea agregar mas columnas ingrese #: ")
        while True:
            nombre_col = input(f"Ingrese el nombre de la columna {i}: ")
            if nombre_col == "#":
                break
            columnas.append(nombre_col)
            i += 1
        Gestor_Base.guardar_objeto(Maestro(nombre, columnas))
        from src.ui_main.Menu_inicial import Menu_inicial
        return Menu_inicial.menu_inicial_Administrativo(cuenta)
