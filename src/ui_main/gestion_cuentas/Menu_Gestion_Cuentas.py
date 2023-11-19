from src.ui_main.gestion_cuentas.Crear_Cuenta import Crear_Cuenta
from src.ui_main.gestion_cuentas.Editar_Cuenta import Editar_Cuenta
from src.ui_main.gestion_cuentas.Ver_Cuenta import Ver_Cuenta


class Menu_Gestion_Cuentas:
    @classmethod
    def menu_gestion_cuentas(cls, cuenta):
        print("1. Crear Cuenta")
        print("2. Editar Cuenta")
        print("3. Ver Cuenta")
        print("4. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            Crear_Cuenta.crear_cuenta()
        if opcion == "2":
            Editar_Cuenta.editar_cuenta(cuenta)
        if opcion == "3":
            Ver_Cuenta.ver_cuenta()
        if opcion == "4":
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()
