from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.gestion_maestros.Editar_Categorias import Editar_Categorias
from src.ui_main.gestion_maestros.Editar_Datos_Basicos_Maestro import Editar_Datos_Basicos_Maestro



class Editar_Maestro:
    @classmethod
    def editar_maestro(cls, cuenta):
        nombre_maestro = input("Ingrese el nombre del maestro que desee ver: ")
        id, maestro = Gestor_Base.buscar_maestro(nombre_maestro)
        print(f"Maestro: {maestro.nombre}")
        print("Columnas:")
        for columna in maestro.columnas:
            print(f"|{columna}|", end=" ")
        print("Categorias:")
        for categoria in maestro.categorias:
            print(f"|{categoria}|", end=" ")
        print("")
        print("Elija una de las siguientes opciones:")
        print("1. Editar Datos Basicos")
        print("2. Editar Categorias")
        if maestro.estado:
            print("3. Deshabilitar")
        else:
            print("3. Habilitar")
        print("4. Volver al menú principal")
        opcion = input()
        if opcion == "1":
            Editar_Datos_Basicos_Maestro.editar_datos_basicos(maestro, cuenta, id)
        if opcion == "2":
            Editar_Categorias.editar_categorias(maestro, cuenta, id)
        if opcion == "3":
            Cambiar_Estado.cambiar_estado(maestro, cuenta, id)
        if opcion == "4":
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo()
