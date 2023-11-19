from src.gestor_aplicacion.Cuenta import Cuenta
from src.ui_main.gestion_cuentas.Menu_Gestion_Cuentas import Menu_Gestion_Cuentas
from src.ui_main.gestion_maestros.Menu_Gestion_Maestros import Menu_Gestion_Maestros

cuenta = Cuenta("Diego", "Gracia", 123, "12/08/2003", "dgraciag", "123", "Administrativo")


class Menu_inicial:
    @classmethod
    def menu_inicial(cls):
        print("1. Gestionar Cuentas")
        print("2. Gestionar Maestros")
        opcion = input("Seleccione una opcion: ")
        print()
        if opcion == "1":
            Menu_Gestion_Cuentas.menu_gestion_cuentas(cuenta)
        if opcion == "2":
            Menu_Gestion_Maestros.menu_gestion_maestros(cuenta)


Menu_inicial.menu_inicial()
