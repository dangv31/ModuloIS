from src.base_datos.Gestor_Base import Gestor_Base


class Ver_Maestro:
    @classmethod
    def ver_maestro(cls, cuenta):
        nombre_maestro = input("Ingrese el nombre del maestro que desee ver: ")
        id, maestro = Gestor_Base.buscar_objeto(nombre_maestro, "Maestro")
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
                return Menu_inicial.menu_inicial_Administrativo()
            else:
                return Menu_inicial.menu_inicial_Clinico()