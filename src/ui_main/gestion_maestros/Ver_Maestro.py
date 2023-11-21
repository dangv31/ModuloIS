from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro


class Ver_Maestro:
    @classmethod
    def ver_maestro(cls, cuenta):
        nombre_maestro = input("Ingrese el nombre del maestro que desee ver: ")
        maestro_l = Gestor_Base.buscar_objeto(nombre_maestro, "Maestro")
        if maestro_l == None:
            if "Administrativo" in cuenta.rol:
                while True:
                    opc_crear = input("No existe el maestro, ¿Desea registrar un maestro (s/n)?")
                    if opc_crear != "s" or opc_crear != "n":
                        print("Ingrese una opcion valida")
                    elif opc_crear == "s":
                        return Crear_Maestro.crear_maestro(cuenta)
                    elif opc_crear == "n":
                        from src.ui_main.Menu_inicial import Menu_inicial
                        return Menu_inicial.menu_inicial_Administrativo(cuenta)
            else:
                print("El maestro no existe")
                from src.ui_main.Menu_inicial import Menu_inicial
                return Menu_inicial.menu_inicial_Administrativo(cuenta)
        id = maestro_l[0]
        maestro = maestro_l[1]
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
                return Menu_inicial.menu_inicial_Administrativo(cuenta)
            else:
                return Menu_inicial.menu_inicial_Clinico(cuenta)