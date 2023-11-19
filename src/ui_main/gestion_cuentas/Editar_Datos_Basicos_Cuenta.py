from src.gestor_aplicacion.Observacion import Observacion


class Editar_Datos_Basicos_Cuenta:
    @classmethod
    def editar_datos_basicos(cls, cuenta_e, cuenta):

        print("Seleccione la opcion que desea realizar: ")
        print("1. Cambiar nombre")
        print("2. Cambiar apellido")
        print("3. Cambiar numero de documento")
        print("4. Cambiar fecha de nacimiento")
        print("5. Cambiar correo")
        print("6. Cambiar rol")
        print("7. Volver al menu inicial")
        print()
        opcion = input()
        if opcion == "1":
            nombre_nuevo = input("Ingrese el nombre nuevo: ")
            cuenta_e.nombres = nombre_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        if opcion == "2":
            apellido_nuevo = input("Ingrese el apellido nuevo: ")
            cuenta_e.apellidos = apellido_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        elif opcion == "3":
            num_documento_nuevo = input("Ingrese el nuevo numero de documento: ")
            cuenta_e.doc = num_documento_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        elif opcion == "4":
            fecha_nacimiento_nueva = input("Ingrese la nueva fecha de nacimiento: ")
            cuenta_e.nacimiento = fecha_nacimiento_nueva
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        elif opcion == "5":
            correo_nuevo = input("Ingrese el nuevo correo: ")
            cuenta_e.correo = correo_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        elif opcion == "6":
            rol = []
            print("1. Administrativo")
            print("2. Clinico")
            print("3. Administrativo-Clinico")
            opc = input("seleccione el rol que tendra el usuario: ")
            if opc == "1":
                rol.append("Administrativo")
            if opc == "2":
                rol.append("Clinico")
            if opc == "3":
                rol.append("Administrativo")
                rol.append("Clinico")

            cuenta_e.rol = rol
            Observacion.generar_observacion(cuenta, cuenta_e)
            print("Cambio realizado con exito!")
            cls.editar_datos_basicos(cuenta_e, cuenta)

        if opcion == "7":
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial()
