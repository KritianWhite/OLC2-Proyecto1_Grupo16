from Patron_Interprete.Abstracto.Instruccion import Intruccion
from Patron_Interprete.Tabla_Simbolos.Tipos import RetornoType
from Patron_Interprete.Expresion.Identificador import Identificador
from Patron_Interprete.Tabla_Simbolos.Simbolos import Simbolos
from Patron_Interprete.Tabla_Simbolos.TablaSimbolos import TablaDeSimbolos as ts

class Asignacion(Intruccion):
    def __init__(self,identificador,valor):
        self.identificador=identificador
        self.valor = valor


    def Ejecutar3D(self, controlador, ts):
        if(ts.Existe_id(self.identificador)):
            codigo = "/*Asignacion*/\n"

            Expression: RetornoType = self.valor.Obtener3D(controlador, ts)
            ValorExpresion = Expression.valor
            TipoExpresion = Expression.tipo
            ts.Actualizar_Simbolo(self.identificador,TipoExpresion,ValorExpresion,ts.name)

            existe_id: Simbolos = ts.ObtenerSimbolo(self.identificador)
            codigo += Expression.codigo + "\n"

            temp1 = controlador.Generador3D.obtenerTemporal()

            codigo += f'\t{temp1} = SP + {existe_id.direccion};\n'
            codigo += f'\tStack[(int){temp1}] = {Expression.temporal};\n'

            #retorno = RetornoType(existe_id.valor)
            #retorno.iniciarRetorno(codigo, "", "", existe_id.tipo)
            return codigo

