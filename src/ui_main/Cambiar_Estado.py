from src.gestor_aplicacion.Observacion import Observacion


class Cambiar_Estado:
    @classmethod
    def cambiar_estado(cls, objeto, cuenta):
        if objeto.estado:
            objeto.estado = False
        else:
            objeto.estado = True
        Observacion.generar_observacion(cuenta, objeto)
        print("Cambio realizado con exito!")