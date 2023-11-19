from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.gestion_cuentas.Buscar_Cuenta import buscar_cuenta
from src.ui_main.gestion_cuentas.Editar_Datos_Basicos_Cuenta import Editar_Datos_Basicos_Cuenta
from src.ui_main.gestion_cuentas.Resetear_Contraseña import Resetear_Contraseña


class Editar_Cuenta:
    @classmethod
    def editar_cuenta(cls, cuenta):
        doc = input("Ingrese el numero de documento de la cuenta: ")
        cuenta_e = buscar_cuenta(doc)
        print(cuenta_e.nombres)
        print(cuenta_e.apellidos)
        print(cuenta_e.doc)
        print()
        print("Elija una de las siguientes opciones:")
        print("1. Editar Datos Basicos")
        print("2. Resetear contraseña")
        if cuenta_e.estado:
            print("3. Deshabilitar")
        else:
            print("3. Habilitar")

        print("4. Volver al menú principal")
        opcion = input()
        if opcion == "1":
            Editar_Datos_Basicos_Cuenta.editar_datos_basicos(cuenta_e, cuenta)
        if opcion == "2":
            Resetear_Contraseña.resetear_contraseña(cuenta_e, cuenta)
        if opcion == "3":
            Cambiar_Estado.cambiar_estado(cuenta_e, cuenta)
        if opcion == "4":
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()
