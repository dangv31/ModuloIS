from src.gestor_aplicacion.Cuenta import Cuenta
from src.ui_main.gestion_maestros.Menu_Gestion_Maestros import Menu_Gestion_Maestros

cuenta = Cuenta("Daniel", "Giraldo", 123)
class Menu_inicial:
    @classmethod
    def menu_inicial(cls):
        print("1. Gestionar Maestros")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            Menu_Gestion_Maestros.menu_gestion_maestros(cuenta)

Menu_inicial.menu_inicial()