from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Sede import Sede
from src.ui_main.gestion_cuentas.Menu_Gestion_Cuentas import Menu_Gestion_Cuentas
from src.ui_main.gestion_maestros.Menu_Gestion_Maestros import Menu_Gestion_Maestros
from src.ui_main.gestion_maestros.Ver_Lista_Maestros import Ver_Lista_Maestros
from src.ui_main.gestion_maestros.Ver_Maestro import Ver_Maestro
from src.ui_main.gestion_sedes.Menu_Gestion_Sede import Menu_Gestion_Sede
from src.ui_main.gestion_sedes.Ver_Lista_Sedes import Ver_Lista_Sedes
from src.ui_main.gestion_sedes.Ver_Sede import Ver_Sede

class Menu_inicial:
    @classmethod
    def menu_inicial_Administrativo(cls, cuenta):
        while True:
            print()
            print("1. Gestionar Cuentas")
            print("2. Gestionar Maestros")
            print("3. Gestionar sedes")
            print("4. Salir")
            opcion = input("Seleccione una opcion: ")
            print()

            if opcion == "1":
                Menu_Gestion_Cuentas.menu_gestion_cuentas(cuenta)
                break
            elif opcion == "2":
                Menu_Gestion_Maestros.menu_gestion_maestros(cuenta)
                break
            elif opcion == "3":
                Menu_Gestion_Sede.menu_gestion_sede(cuenta)
                break
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    @classmethod
    def menu_inicial_Clinico(cls, cuenta):
        while True:
            print()
            print("1. Ver Maestro")
            print("2. Ver sede")
            print("3. Ver Lista de  Maestros")
            print("4. Ver Lista de  Sedes")
            print("5. Salir")
            opcion = input("Seleccione una opcion: ")
            print()

            if opcion == "1":
                Ver_Maestro.ver_maestro(cuenta)
                break
            elif opcion == "2":
                Ver_Sede.ver_sede(cuenta)
                break
            elif opcion == "3":
                Ver_Lista_Maestros.ver_lista_maestros(cuenta)
                break
            elif opcion == "4":
                Ver_Lista_Sedes.ver_lista_sedes(cuenta)
                break
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

