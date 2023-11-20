from src.gestor_aplicacion.Sede import Sede


class Ver_Lista_Sedes:
    @classmethod
    def ver_lista_sedes(cls, cuenta):
        indice = 1
        for sede in Sede.lista_sedes:
            print()
            print(f"Sede {indice}:")
            sede.imprimir_info()
            print()
            indice +=1
        print()
        entrada = input("Ingrese cualquier caracter para volver al menu incial ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            if "Administrativo" in cuenta.rol:
                Menu_inicial.menu_inicial_Administrativo()
            else:
                Menu_inicial.menu_inicial_Clinico()
