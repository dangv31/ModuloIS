from src.ui_main.Menu_inicial import Menu_inicial
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.gestion_maestros.Editar_Maestro import Editar_Maestro
from src.ui_main.gestion_maestros.Ver_Maestro import Ver_Maestro


class Menu_Gestion_Maestros:
    @classmethod
    def menu_gestion_maestros(cls, cuenta):
        print("1. Crear Maestro")
        print("2. Editar Maestro")
        print("3. Ver Maestro")
        print("4. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            Crear_Maestro.crear_maestro()
        if opcion == "2":
            Editar_Maestro.editar_maestro(cuenta)
        if opcion == "3":
            Ver_Maestro.ver_maestro()
        if opcion == "4":
            Menu_inicial.menu_inicial()