from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Cuenta import Cuenta


class Crear_Cuenta:
    @classmethod
    def crear_cuenta(cls, cuenta):
        global doc
        print()
        print("Por favor, ingrese la siguiente informacion sobre el usuario a crear: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        while True:
            try:
                doc = int(input("Numero de documento: "))
            except ValueError:
                print("Error: Numero de documento debe ser un valor numérico. Intente de nuevo.")
            id, cuenta_e = Gestor_Base.buscar_objeto(doc, "Cuenta")
            if cuenta_e is None:
                break
            else:
                print("Ya hay una cuenta creada con este numero de documento")

        nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
        correo = input("correo: ")
        contrasena = input("Contraseña: ")

        cuenta_creada = Cuenta(nombre, apellido, doc, nacimiento, correo, contrasena)

        while True:
            print("1. Administrativo")
            print("2. Clinico")
            print("3. Administrativo-Clinico")
            opc = int(input("Seleccione el rol que tendrá el usuario: "))
            if opc in [1, 2, 3]:
                if opc == 1 and "Administrativo" in cuenta.rol:
                    cuenta_creada.rol.append("Administrativo")
                    break
                elif opc == 2 and "Clinico" in cuenta.rol:
                    cuenta_creada.rol.append("Clinico")
                    break
                elif opc == 3 and "Administrativo" in cuenta.rol and "Clinico" in cuenta.rol:
                    cuenta_creada.rol.append("Administrativo")
                    cuenta_creada.rol.append("Clinico")
                    break
                else:
                    print("no tienes permiso para crear una cuenta con este rol")
                    print()
            else:
                print("Error: Rol seleccionado no válido. Intente de nuevo.")

        while True:
                print("1. Medellin")
                print("2. Manizales")
                print("3. Bogota")
                print("4. Medellin-Manizales-Bogota")
                opc = int(input("Seleccione la sede en donde estará el usuario: "))
                if opc in [1, 2, 3, 4]:
                    if opc == 1:
                        id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                        if sede in cuenta.sede:
                            cuenta_creada.sede.append(sede)
                            sede.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede, id_sede)
                            break
                        else:
                            print("no tienes permiso para crear una cuenta en esta sede")
                            print()

                    if opc == 2:
                        id_sede2, sede2 = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                        if sede2 in cuenta.sede:
                            cuenta_creada.sede.append(sede2)
                            sede2.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede2, id_sede2)
                            break
                        else:
                            print("no tienes permiso para crear una cuenta en esta sede")
                            print()
                    if opc == 3:
                        id_sede3, sede3 = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                        if sede3 in cuenta.sede:
                            cuenta_creada.sede.append(sede3)
                            sede3.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede3, id_sede3)
                            break
                        else:
                            print("no tienes permiso para crear una cuenta en esta sede")
                            print()
                    if opc == 4:
                        id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                        id_sede2, sede2 = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                        id_sede3, sede3 = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                        if sede in cuenta.sede and sede2 in cuenta.sede and sede3 in cuenta.sede:
                            cuenta_creada.sede.append(sede)
                            sede.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede, id_sede)
                            cuenta_creada.sede.append(sede2)
                            sede2.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede2, id_sede2)
                            cuenta_creada.sede.append(sede3)
                            sede3.personal.append(cuenta_creada)
                            Gestor_Base.actualizar_objeto(sede3, id_sede3)
                            break
                        else:
                            print("no tienes permiso para crear una cuenta en estas sedes")
                            print()
                else:
                    print("Error: Sede seleccionada no válida. Intente de nuevo.")

        Gestor_Base.guardar_objeto(cuenta_creada)
        print()
        print("¡Registro exitoso!")
        print()
        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial_Administrativo(cuenta)
