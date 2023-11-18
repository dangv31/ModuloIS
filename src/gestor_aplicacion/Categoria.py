class Categoria():
    def __init__(self, informacion, maestro):
        self.info = informacion
        self.maestro = maestro
        self.estado = True
        self.maestro.categorias.append(self)
        