from src.gestor_aplicacion.Cuenta import Cuenta
from src.ui_main.Menu_inicial import Menu_inicial


class Inicio_sesion:
    @classmethod
    def inicio_sesion(cls):
        correo_ingresado = input("Ingrese su correo: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")

        for cuenta in Cuenta.lista_cuentas:
            if cuenta.correo == correo_ingresado and cuenta.contraseña == contraseña_ingresada and "Administrativo" in cuenta.rol:
                print(f"¡Bienvenido {cuenta.nombres}!")
                Menu_inicial.menu_inicial_Administrativo()

            if cuenta.correo == correo_ingresado and cuenta.contraseña == contraseña_ingresada and "Administrativo" not in cuenta.rol:
                print(f"¡Bienvenido {cuenta.nombres}!")
                Menu_inicial.menu_inicial_Clinico()

Inicio_sesion.inicio_sesion()