class Cuenta():
    lista_cuentas = []
    def __init__(self, nombres, apellidos, doc, nacimiento,  correo, contraseña, rol):
        self.nombres = nombres
        self.apellidos = apellidos
        self.doc = doc
        self.nacimiento = nacimiento
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol
        self.estado = True
        self.observaciones = []