from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Sede import Sede


class Crear_Cuenta:
    @classmethod
    def crear_cuenta(cls, cuenta):
        print()
        print("Por favor, ingrese la siguiente informacion sobre el usuario a crear: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        doc = int(input("Numero de documento: "))
        nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
        correo = input("correo: ")
        contrasena = input("Contraseña: ")

        cuenta_creada = Cuenta(nombre, apellido, doc, nacimiento, correo, contrasena)

        print("1. Administrativo")
        print("2. Clinico")
        print("3. Administrativo-Clinico")
        opc = input("seleccione el rol que tendra el usuario: ")
        if opc == "1" and "Administrativo" in cuenta.rol:
            cuenta_creada.rol.append("Administrativo")
        elif opc == "2" and "Clinico" in cuenta.rol:
            cuenta_creada.rol.append("Clinico")
        elif opc == "3" and "Administrativo" in cuenta.rol and "Clinico" in cuenta.rol:
            cuenta_creada.rol.append("Administrativo")
            cuenta_creada.rol.append("Clinico")
        else:
            print("no tienes permiso para crear una cuenta con este rol")
            print()
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta)

        print("1. Medellin")
        print("2. Manizales")
        print("3. Bogota")
        print("4. Medellin-Manizales-Bogota")

        opc = input("seleccione la sede en donde estara el usuario: ")
        if opc == "1":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Medellin":
                    if sede in cuenta.sede:
                        cuenta_creada.sede.append(sede)
                        sede.personal.append(cuenta_creada)
                    else:
                        print("no tienes permiso para crear una cuenta en esta sede")
                        print()
                        from src.ui_main.Menu_inicial import Menu_inicial
                        Menu_inicial.menu_inicial_Administrativo(cuenta)

        if opc == "2":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Manizales":
                    if sede in cuenta.sede:
                        cuenta_creada.sede.append(sede)
                        sede.personal.append(cuenta_creada)
                    else:
                        print("no tienes permiso para crear una cuenta en esta sede")
                        print()
                        from src.ui_main.Menu_inicial import Menu_inicial
                        Menu_inicial.menu_inicial_Administrativo(cuenta)
        if opc == "3":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Bogota":
                    if sede in cuenta.sede:
                        cuenta_creada.sede.append(sede)
                        sede.personal.append(cuenta_creada)
                    else:
                        print("no tienes permiso para crear una cuenta en esta sede")
                        print()
                        from src.ui_main.Menu_inicial import Menu_inicial
                        Menu_inicial.menu_inicial_Administrativo(cuenta)
        if opc == "4":
            for sede in Sede.lista_sedes:
                if sede in cuenta.sede:
                    cuenta_creada.sede.append(sede)
                    sede.personal.append(cuenta_creada)
                else:
                    print("no tienes permiso para crear una cuenta en esta sede")
                    print()
                    from src.ui_main.Menu_inicial import Menu_inicial
                    Menu_inicial.menu_inicial_Administrativo(cuenta)

        Gestor_Base.guardar_objeto(cuenta_creada)
        print()
        print("¡Registro exitoso!")
        print()
        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial_Administrativo(cuenta)
