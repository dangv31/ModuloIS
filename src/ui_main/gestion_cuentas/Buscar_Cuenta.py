from src.gestor_aplicacion.Cuenta import Cuenta


def buscar_cuenta(doc):
    for cuenta in Cuenta.lista_cuentas:
        if cuenta.doc == doc:
            return cuenta
        else:
            return False
