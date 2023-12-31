from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.Menu_inicial import Menu_inicial

class Inicio_sesion:
    @classmethod
    def inicio_sesion(cls):
        while True:
            print()
            correo_ingresado = input("Ingrese su correo: ")
            contrasena_ingresada = input("Ingrese su contraseña: ")

            cuenta_encontrada = None
            lista_cuentas = Gestor_Base.lista_cuentas()

            for id, cuenta in lista_cuentas:
                if cuenta.correo == correo_ingresado and cuenta.contrasena == contrasena_ingresada:
                    cuenta_encontrada = cuenta
                    break

            if cuenta_encontrada:
                if cuenta_encontrada.estado:
                    if "Administrativo" in cuenta_encontrada.rol:
                        print()
                        print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                        Menu_inicial.menu_inicial_Administrativo(cuenta_encontrada)
                    else:
                        print()
                        print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                        Menu_inicial.menu_inicial_Clinico(cuenta_encontrada)
                    break
                else:
                    print()
                    print("Su cuenta esta deshabilitada")
                    opcion = input("¿Desea intentarlo de nuevo? (s/n): ").lower()
                    if opcion != 's':
                        print("Saliendo del programa. ¡Hasta luego!")
                        break

            else:
                print()
                print("Error: Correo o contraseña incorrectos.")
                opcion = input("¿Desea intentarlo de nuevo? (s/n): ").lower()
                if opcion != 's':
                    print("Saliendo del programa. ¡Hasta luego!")
                    break


Inicio_sesion.inicio_sesion()
