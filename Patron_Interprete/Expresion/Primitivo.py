from Patron_Interprete.Abstracto.Instruccion import Intruccion
from Patron_Interprete.Tabla_Simbolos.Tipos import Tipos
from Patron_Interprete.Expresion.Value import Value
from Patron_Interprete.Controlador import Controlador

class Primitivo (Intruccion):
    def __init__(self, fila, columna, tipo:Tipos , valor):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno, listaMensajes):
        
        return self.valor

    def getTipo(self):
        return self.tipo

    def traducir(self, entorno , manejador):

        newValue = Value(None) 
        
        newValue.Value = str(self.valor)
        newValue.isTemp = False
        newValue.Tipo = self.tipo
        newValue.TrueLabel = ""
        newValue.FalseLabel = ""

        return newValue