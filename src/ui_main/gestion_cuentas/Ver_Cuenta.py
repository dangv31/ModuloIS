from src.base_datos.Gestor_Base import Gestor_Base


class Ver_Cuenta:
    @classmethod
    def ver_cuenta(cls, cuenta_principal):
        doc = int(input("Ingrese el numero de documento de la cuenta que desea ver: "))
        id, cuenta = Gestor_Base.buscar_objeto(doc, "Cuenta")
        print("Nombre:", cuenta.nombres)
        print("Apellido:",cuenta.apellidos)
        print("Numero de docmuento:",cuenta.doc)
        print("Fecha de nacimiento:",cuenta.nacimiento)
        print("Correo:",cuenta.correo)
        print("Rol:", end=" ")
        for rol in cuenta.rol:
            print(rol, end=" ")
        print()
        if cuenta.estado:
            print("Estado: Habilitada")
        else:
            print("Estado: Deshabilitada")
        print("Sede:", end=" ")
        for sede in cuenta.sede:
            print(sede.nombre, end=" ")
        print()

        print()

        entrada = input("Ingrese cualquier caracter para volver al menu incial ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta_principal)