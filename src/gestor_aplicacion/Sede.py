class Sede:
    def __init__(self, nombre, quirofanos, salas_de_espera, consultorios,
                 direccion, pacientes, sillas, camas, ambulancias):
        self.nombre = nombre
        self.quirofanos = quirofanos
        self.salas_de_espera = salas_de_espera
        self.personal = []
        self.consultorios = consultorios
        self.direccion = direccion
        self.pacientes = pacientes
        self.sillas = sillas
        self.camas = camas
        self.ambulancias = ambulancias
        self.estado = True
        self.observaciones = []