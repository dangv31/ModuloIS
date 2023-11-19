from src.ui_main.gestion_cuentas.Buscar_Cuenta import buscar_cuenta


class Ver_Cuenta:
    @classmethod
    def ver_cuenta(cls):
        doc = input("Ingrese el numero de documento de la cuenta que desea ver: ")
        cuenta = buscar_cuenta(doc)
        print("Nombre:", cuenta.nombres)
        print("Apellido:",cuenta.apellidos)
        print("Numero de docmuento:",cuenta.doc)
        print("Fecha de nacimiento:",cuenta.nacimiento)
        print("Correo:",cuenta.correo)
        print("Rol:", ' '.join(cuenta.rol))
        if cuenta.estado:
            print("Estado: Habilitada")
        else:
            print("Estado: Deshabilitada")
        print("Sede:", ' '.join(cuenta.sede))
        print()

        entrada = input("Ingrese cualquier caracter para volver al menu incial ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()