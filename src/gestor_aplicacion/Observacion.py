class Observacion:
    def __init__(self, cuenta, detalle):
        self.cuenta = cuenta
        self.detalle = detalle

    def __str__(self):
        return f"Cuenta que realizo esta observacion: {self.cuenta}\n Detalle: {self.detalle}"

    @classmethod
    def generar_observacion(cls, cuenta, objeto):
        detalle = input("Ingrese el motivo de los cambios:")
        objeto.observaciones.append(Observacion(cuenta, detalle))
        print("Observacion Registrada!")
