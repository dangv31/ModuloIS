from src.ui_main.gestion_maestros.Buscar_Maestro import buscar_maestro


class Ver_Maestro:
    @classmethod
    def ver_maestro(cls, cuenta):
        nombre_maestro = input("Ingrese el nombre del maestro que desee ver: ")
        maestro = buscar_maestro(nombre_maestro)
        print(f"Nombre: {maestro.nombre}")
        print("Columnas: ")
        for columna in maestro.columnas:
            print(columna, end=" ")
        print("")
        print("Categorias")
        for categoria in maestro.categorias:
            print(categoria)
        print("Observaciones")
        for observacion in maestro.observaciones:
            print(observacion)
        entrada = input("Ingrese cualquier caracter para volver al menu incial: ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            if "Administrativo" in cuenta.rol:
                Menu_inicial.menu_inicial_Administrativo()
            else:
                Menu_inicial.menu_inicial_Clinico()