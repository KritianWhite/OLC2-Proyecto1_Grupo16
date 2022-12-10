from Patron_Interprete.Tabla_Simbolos.Tipos import Tipo
from Patron_Interprete.Entorno import Entorno
from Patron_Interprete.Tabla_Simbolos.Simbolos import Simbolos
from Patron_Interprete.Abstracto.Instruccion import Intruccion


class Identificador(Intruccion):
    def __init__(self, fila, columna, identificador):
        self.identificador =  identificador
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULLO

    def ejecutar(self, entorno:Entorno , listaMensajes):
        simbolo : Simbolos=entorno.buscarSimbolo(self.identificador)

        if simbolo != None:
            self.tipo =  simbolo.tipo
            return simbolo.valor
        return None

    def traducir(self, entorno, manejador):
        print("ide")

    def getTipo(self):
        return self.tipo