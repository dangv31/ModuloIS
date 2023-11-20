from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion
from src.gestor_aplicacion.Sede import Sede


class Editar_Datos_Basicos_Cuenta:
    @classmethod
    def editar_datos_basicos(cls, cuenta_e, cuenta, id):

        print("Seleccione la opcion que desea realizar: ")
        print("1. Cambiar nombre")
        print("2. Cambiar apellido")
        print("3. Cambiar numero de documento")
        print("4. Cambiar fecha de nacimiento")
        print("5. Cambiar correo")
        print("6. Cambiar rol")
        print("7. Cambiar sede")
        print("8. Volver al menu inicial")
        print()
        opcion = input()
        if opcion == "1":
            nombre_nuevo = input("Ingrese el nombre nuevo: ")
            cuenta_e.nombres = nombre_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        if opcion == "2":
            apellido_nuevo = input("Ingrese el apellido nuevo: ")
            cuenta_e.apellidos = apellido_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        elif opcion == "3":
            num_documento_nuevo = input("Ingrese el nuevo numero de documento: ")
            cuenta_e.doc = num_documento_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        elif opcion == "4":
            fecha_nacimiento_nueva = input("Ingrese la nueva fecha de nacimiento: ")
            cuenta_e.nacimiento = fecha_nacimiento_nueva
            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        elif opcion == "5":
            correo_nuevo = input("Ingrese el nuevo correo: ")
            cuenta_e.correo = correo_nuevo
            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        elif opcion == "6":
            print("1. Administrativo")
            print("2. Clinico")
            print("3. Administrativo-Clinico")
            opc = input("seleccione el rol que tendra el usuario: ")
            cuenta_e.rol.clean()
            if opc == "1":
                cuenta_e.rol.append("Administrativo")
            if opc == "2":
                cuenta_e.rol.append("Clinico")
            if opc == "3":
                cuenta_e.rol.append("Administrativo")
                cuenta_e.rol.append("Clinico")

            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        elif opcion == "7":
            for sede in Sede.lista_sedes:
                if cuenta_e in sede.personal:
                    sede.personal.remove(cuenta_e)
            print("1. Medellin")
            print("2. Manizales")
            print("3. Bogota")
            print("3. Medellin-Manizales-Bogota")
            opc = input("seleccione la sede en donde estara el usuario: ")
            cuenta_e.sede.clean()
            if opc == "1":
                id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                cuenta_e.sede.append(sede)
                sede.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede, id_sede)
            if opc == "2":
                id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                cuenta_e.sede.append(sede)
                sede.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede, id_sede)
            if opc == "3":
                id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                cuenta_e.sede.append(sede)
                sede.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede, id_sede)
            if opc == "4":
                id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                cuenta_e.sede.append(sede)
                sede.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede, id_sede)
                id_sede2, sede2 = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                cuenta_e.sede.append(sede2)
                sede2.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede2, id_sede2)
                id_sede3, sede3 = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                cuenta_e.sede.append(sede3)
                sede3.personal.append(cuenta_e)
                Gestor_Base.actualizar_objeto(sede3, id_sede3)

            Observacion.generar_observacion(cuenta, cuenta_e)
            Gestor_Base.actualizar_objeto(cuenta_e, id)
            print("Cambio realizado con exito!")
            return cls.editar_datos_basicos(cuenta_e, cuenta, id)

        if opcion == "8":
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta)
