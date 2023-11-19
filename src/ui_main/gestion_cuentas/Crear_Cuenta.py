from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Sede import Sede


class Crear_Cuenta:
    @classmethod
    def crear_cuenta(cls):
        print()
        print("Por favor, ingrese la siguiente informacion sobre el usuario a crear: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        doc = int(input("Numero de documento: "))
        nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
        correo = input("correo: ")
        contraseña = input("Contraseña: ")

        cuenta_creada = Cuenta(nombre, apellido, doc, nacimiento, correo, contraseña)

        print("1. Administrativo")
        print("2. Clinico")
        print("3. Administrativo-Clinico")
        opc = input("seleccione el rol que tendra el usuario: ")
        if opc == "1":
            cuenta_creada.rol.append("Administrativo")
        if opc == "2":
            cuenta_creada.rol.append("Clinico")
        if opc == "3":
            cuenta_creada.rol.append("Administrativo")
            cuenta_creada.rol.append("Clinico")

        print("1. Medellin")
        print("2. Manizales")
        print("3. Bogota")
        print("3. Medellin-Manizales-Bogota")

        opc = input("seleccione la sede en donde estara el usuario: ")
        if opc == "1":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Medellin":
                    cuenta_creada.sede.append(sede)
                    sede.personal.append(cuenta_creada)

        if opc == "2":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Manizales":
                    cuenta_creada.sede.append(sede)
                    sede.personal.append(cuenta_creada)
        if opc == "3":
            for sede in Sede.lista_sedes:
                if sede.nombre == "MedPLus Bogota":
                    cuenta_creada.sede.append(sede)
                    sede.personal.append(cuenta_creada)
        if opc == "4":
            for sede in Sede.lista_sedes:
                cuenta_creada.sede.append(sede)
                sede.personal.append(cuenta_creada)

        Cuenta.lista_cuentas.append(cuenta_creada)
        print()
        print("¡Registro exitoso!")
        print()
        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial()
