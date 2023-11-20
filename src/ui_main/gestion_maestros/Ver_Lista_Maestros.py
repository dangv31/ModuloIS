from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Maestro import Maestro


class Ver_Lista_Maestros:
    @classmethod
    def ver_lista_maestros(cls, cuenta):
        indice = 1
        for maestro in Maestro.lista_maestros:
            print()
            print(f"Maestro {indice}:")
            print(f"Nombre: {maestro.nombre}")
            print("Columnas: ")
            for columna in maestro.columnas:
                print(columna, end=" ")
            print("")
            print("Categorias")
            for categoria in maestro.categorias:
                print(categoria)
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
