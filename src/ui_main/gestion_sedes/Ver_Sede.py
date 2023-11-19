from src.ui_main.gestion_sedes.Buscar_Sede import buscar_sede
from src.gestor_aplicacion.Sede import Sede


class Ver_Sede:
    @classmethod
    def ver_sede(cls, cuenta):
        sede = buscar_sede()
        sede.imprimir_info()
        print("Observaciones: ")
        for observacion in sede.observaciones:
            print(observacion)
        entrada = input("Ingrese cualquier caracter para volver al menu incial: ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()
