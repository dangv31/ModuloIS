from src.base_datos.maestros import crear_tabla_maestro
class Crear_Maestro:
    @classmethod
    def crear_maestro(cls):
        nombre = input("Ingrese el nombre del maestro: ")
        i = 1
        columnas = []
        print("Ingrese el nombre de las columnas, si no desea agregar mas columnas ingrese #")
        while True:
            nombre_col = input(f"Ingrese el nombre de la columna {i}: ")
            if nombre_col == "#":
                break
            print("Ingrese el tipo de dato de la columna:\n"
                  "TEXT: Para textos\n"
                  "INTEGER: Para numeros sin decimales\n"
                  "REAL: Para numeros con decimales")
            tipo_col = input()

            columnas.append(nombre_col + " " + tipo_col)
            i += 1

        crear_tabla_maestro(nombre, columnas)
