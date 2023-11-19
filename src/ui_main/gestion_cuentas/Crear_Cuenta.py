from src.gestor_aplicacion.Cuenta import Cuenta


class Crear_Cuenta:
    @classmethod
    def crear_cuenta(cls):
        print()
        print("Por favor, ingrese la siguiente informacion sobre el usuario a crear: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        doc = input("Numero de documento: ")
        nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
        correo = input("correo: ")
        contraseña = input("Contraseña: ")
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

        sede = []
        print("1. Medellin")
        print("2. Manizales")
        print("3. Bogota")
        print("3. Medellin-Manizales-Bogota")

        opc = input("seleccione la sede en donde estara el usuario: ")
        if opc == "1":
            sede.append("Medellin")
        if opc == "2":
            sede.append("Manizales")
        if opc == "3":
            sede.append("Bogota")
        if opc == "4":
            sede.append("Medellin")
            sede.append("Manizales")
            sede.append("Bogota")

        Cuenta.lista_cuentas.append(Cuenta(nombre,apellido,doc,nacimiento,correo,contraseña, rol, sede))
        print()
        print("¡Registro exitoso!")
        print()
        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial()
