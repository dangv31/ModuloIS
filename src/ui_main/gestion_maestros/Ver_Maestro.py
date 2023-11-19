from src.ui_main.gestion_maestros.Buscar_Maestro import buscar_maestro


class Ver_Maestro:
    @classmethod
    def ver_maestro(cls):
        nombre_maestro = input("Ingrese el nombre del maestro que desee ver: ")
        maestro = buscar_maestro(nombre_maestro)
        print(maestro.nombre)
        for columna in maestro.columnas:
            print(columna, end=" ")
        print("")
        for categoria in maestro.categorias:
            print(categoria)
        entrada = input("Ingrese cualquier caracter para volver al menu incial")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()