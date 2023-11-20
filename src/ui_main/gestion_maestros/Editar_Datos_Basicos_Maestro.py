from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion


class Editar_Datos_Basicos_Maestro:
    @classmethod
    def editar_datos_basicos(cls, maestro, cuenta, id):
        print(maestro.nombre)
        for index, columna in enumerate(maestro.columnas):
            print(f"{index+1}.{columna}")
        print("Seleccione la opcion que desea realizar: ")
        print("1. Cambiar Nombre")
        print("2. Cambiar nombre de alguna columna")
        print("3. Volver al menu inicial")
        opcion = input()
        if opcion == "1":
            nombre_nuevo = input("Ingrese el nombre nuevo: ")
            maestro.nombre = nombre_nuevo
            Observacion.generar_observacion(cuenta, maestro)
            Gestor_Base.actualizar_objeto(maestro, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(maestro, cuenta, id)
        if opcion == "2":
            while True:
                columnas = maestro.columnas
                for index, columna in enumerate(columnas):
                    print(f"{index + 1}.{columna}")
                index_columna = input("Ingrese el numero del indice de la columna para cambiar el nombre o # para terminar el proceso: ")
                if index_columna == "#":
                    break
                index_columna = int(index_columna)
                nombre_col = input(f"Ingrese el nombre nuevo de la columna {index_columna}: ")
                columnas[index_columna - 1] = nombre_col
            Observacion.generar_observacion(cuenta, maestro)
            Gestor_Base.actualizar_objeto(maestro, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(maestro, cuenta, id)
        if opcion == "3":
            from src.ui_main.Menu_inicial import Menu_inicial
            return Menu_inicial.menu_inicial_Administrativo(cuenta)
