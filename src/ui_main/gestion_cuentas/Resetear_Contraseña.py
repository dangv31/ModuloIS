from src.gestor_aplicacion.Observacion import Observacion


class Resetear_Contraseña:
    @classmethod
    def resetear_contraseña(cls, cuenta_e, cuenta):
        contraseña_nueva = input("Ingrese la nueva contraseña: ")
        confirmar_contraseña = input("Confirme la nueva contraseña: ")

        if contraseña_nueva == confirmar_contraseña:
            cuenta_e.contraseña = contraseña_nueva
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")

        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial()