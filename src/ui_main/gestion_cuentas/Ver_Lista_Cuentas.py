from src.gestor_aplicacion.Cuenta import Cuenta


class Ver_Lista_Cuentas:
    @classmethod
    def ver_lista_cuentas(cls):
        indice = 1
        for cuenta in Cuenta.lista_cuentas:
            print()
            print(f"Cuenta {indice}:")
            print("Nombre:", cuenta.nombres)
            print("Apellido:",cuenta.apellidos)
            print("Numero de docmuento:",cuenta.doc)
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
            indice +=1
        print()
        entrada = input("Ingrese cualquier caracter para volver al menu incial ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo()