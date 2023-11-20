from src.gestor_aplicacion.Cuenta import Cuenta
from src.ui_main.Menu_inicial import Menu_inicial

class Inicio_sesion:
    @classmethod
    def inicio_sesion(cls):
        while True:
            print()
            correo_ingresado = input("Ingrese su correo: ")
            contraseña_ingresada = input("Ingrese su contraseña: ")

            cuenta_encontrada = None

            for cuenta in Cuenta.lista_cuentas:
                if cuenta.correo == correo_ingresado and cuenta.contraseña == contraseña_ingresada:
                    cuenta_encontrada = cuenta
                    break

            if cuenta_encontrada:
                if "Administrativo" in cuenta_encontrada.rol:
                    print()
                    print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                    Menu_inicial.menu_inicial_Administrativo()
                else:
                    print()
                    print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                    Menu_inicial.menu_inicial_Clinico()
                break
            else:
                print()
                print("Error: Correo o contraseña incorrectos.")
                opcion = input("¿Desea intentarlo de nuevo? (s/n): ").lower()
                if opcion != 's':
                    print("Saliendo del programa. ¡Hasta luego!")
                    break

Inicio_sesion.inicio_sesion()
