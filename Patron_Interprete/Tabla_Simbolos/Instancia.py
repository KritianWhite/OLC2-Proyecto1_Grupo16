from Patron_Interprete.Tabla_Simbolos.Simbolos import Simbolos
from Patron_Interprete.Tabla_Simbolos.Tipos import tipo as t

class Instancia(Simbolos):

    def __init__(self,idClase, idInstancia, entornoInstancia):
        super().__init__()
        super().iniciarSimboloInstancia(idClase, idInstancia, entornoInstancia, t.OBJETO)