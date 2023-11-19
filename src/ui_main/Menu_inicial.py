from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Sede import Sede
from src.ui_main.gestion_cuentas.Menu_Gestion_Cuentas import Menu_Gestion_Cuentas
from src.ui_main.gestion_maestros.Menu_Gestion_Maestros import Menu_Gestion_Maestros
from src.ui_main.gestion_sedes.Menu_Gestion_Sede import Menu_Gestion_Sede

cuenta = Cuenta("Diego", "Gracia", 123, "12/08/2003", "dgraciag", "123", "Administrativo", "Medellin")

sede = Sede("MedPLus", 100, 100, 100, "Medelln", 100, 100, 100, 100)
Sede.lista_sedes.append(sede)
class Menu_inicial:
    @classmethod
    def menu_inicial(cls):
        print("1. Gestionar Cuentas")
        print("2. Gestionar Maestros")
        print("3. Gestionar sedes")
        opcion = input("Seleccione una opcion: ")
        print()
        if opcion == "1":
            Menu_Gestion_Cuentas.menu_gestion_cuentas(cuenta)
        if opcion == "2":
            Menu_Gestion_Maestros.menu_gestion_maestros(cuenta)
        if opcion == "3":
            Menu_Gestion_Sede.menu_gestion_sede(cuenta)


Menu_inicial.menu_inicial()
