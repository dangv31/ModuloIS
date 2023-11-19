from src.gestor_aplicacion.Cuenta import Cuenta


def buscar_cuenta(doc):
    for i in range(len(Cuenta.lista_cuentas)):
        if Cuenta.lista_cuentas[i].doc == str(doc):
            return Cuenta.lista_cuentas[i]
        else:
            return False
