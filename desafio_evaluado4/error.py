# Grupo 3: Lolet Llanquinao - Juan Torres . Leonardo llaupen - Claudio Méndez

class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension : dimension
        self.maximo = maximo
        
    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            mansaje = self.mensaje