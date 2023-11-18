from src.gestor_aplicacion.Maestro import Maestro
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.Menu_inicial import Menu_inicial
from src.ui_main.gestion_maestros.Buscar_Maestro import buscar_maestro
from src.ui_main.gestion_maestros.Editar_Categorias import Editar_Categorias
from src.ui_main.gestion_maestros.Editar_Datos_Basicos_Maestro import Editar_Datos_Basicos_Maestro


class Editar_Maestro:
    @classmethod
    def editar_maestro(cls, cuenta):
        nombre = input("Ingrese el nombre del maestro: ")
        maestro = buscar_maestro(nombre)
        print(maestro.nombre)
        for columna in maestro.columnas:
            print(columna, end="")
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
            Editar_Datos_Basicos_Maestro.editar_datos_basicos(maestro, cuenta)
        if opcion == "2":
            Editar_Categorias.editar_categorias(maestro, cuenta)
        if opcion == "3":
            Cambiar_Estado.cambiar_estado(maestro, cuenta)
        if opcion == "4":
            Menu_inicial.menu_inicial()
