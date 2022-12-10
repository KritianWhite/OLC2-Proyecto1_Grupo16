
from Patron_Interprete.Abstracto.Instruccion import Intruccion
from Patron_Interprete.Tabla_Simbolos.Tipos import Tipos
from Patron_Interprete.Expresion.Value import Value

class Aritmetica (Intruccion):

    def __init__(self, expresion_1,expresion_2, operador, fila, columna, es_tipo=None):
        self.fila = fila
        self.columna = columna
        self.expresion_1 = expresion_1
        self.expresion_2 = expresion_2
        self.operador = operador
        self.tipo =Tipos.UNDEFINED
        self.es_tipo = es_tipo


    def ejecutar(self, entorno, listaMensajes):
       print("ejecutar")

    def traducir(self, ent, man):
        retorno_izq = Value()
        retorno_der = Value()

        retorno_izq = self.expresion_1.traducir(ent , man)
        retorno_der = self.expresion_2.traducir(ent , man)

        nuevo_temporal = man.nuevo_temp()
        
        if self.operador == "+" or self.operador == "-" or self.operador == "/" or self.operador == "*":
            man.agregar_aritmetica(nuevo_temporal, retorno_izq.Value , retorno_der.Value , self.operador)
            nuevoValue  = Value()
            nuevoValue.Value = nuevo_temporal
            nuevoValue.isTemp = True
            nuevoValue.Tipo = self.tipo
            nuevoValue.TrueLabel = ""
            nuevoValue.FalseLabel = ""
            return  nuevoValue
        elif self.operador == "pow":
            print("potencia")
            print(retorno_izq)
            man.potencia(retorno_izq.Value,retorno_der.Value)
        elif self.operador == "%":
            man.modulo(retorno_izq.Value , retorno_der.Value)