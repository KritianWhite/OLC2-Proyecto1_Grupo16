from Patron_Interprete.Abstracto.Instruccion import Intruccion
from Patron_Interprete.Expresion import Identificador
from Patron_Interprete.Tabla_Simbolos.Simbolos import Simbolos
from Patron_Interprete.Tabla_Simbolos.Tipos import tipo, RetornoType

class Declaracion(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo


    def Ejecutar3D(self, controlador, ts):
        print(" ==== Declarar === ",self.expresion)
        codigo = ""
        if self.expresion is not None:

            return_exp: RetornoType = self.expresion.Obtener3D(controlador, ts)

            if self.tipo is not None:
                sizeTabla = ts.size
                temp1 = controlador.Generador3D.obtenerTemporal()
                codigo += "/*Declaracion*/\n"
                codigo += return_exp.codigo + "\n"
                codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                codigo += f'\tStack[(int){temp1}] = {return_exp.temporal};\n'
                ts.size += 1

                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id,return_exp.valor, self.tipo, self.mut,sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                return codigo
                #controlador.Generador3D.agregarInstruccion(codigo)

            else:
                #ValorExpresion = return_exp.valor
                TipoExpresion = return_exp.tipo
                self.tipo = TipoExpresion
                sizeTabla = ts.size
                temp1 = controlador.Generador3D.obtenerTemporal()
                codigo += "/*Declaracion*/\n"
                codigo += return_exp.codigo + "\n"
                codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                codigo += f'\tStack[(int){temp1}] = {return_exp.temporal};\n'
                ts.size += 1

                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, self.tipo, self.mut, sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                return codigo
                #controlador.Generador3D.agregarInstruccion(codigo)

        else:

            if self.tipo is not None:
                sizeTabla = ts.size
                newSimbolo = Simbolos()
                if self.tipo == tipo.ENTERO:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += "/*Declaracion*/\n"
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = 0;\n'
                    ts.size += 1

                    newSimbolo.SimboloPremitivo(self.identificador.id, 0, self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return  codigo

                elif self.tipo == tipo.DECIMAL:
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0.0, self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.CARACTER:
                    newSimbolo.SimboloPremitivo(self.identificador.id, '', self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.STRING or self.tipo == tipo.DIRSTRING:
                    newSimbolo.SimboloPremitivo(self.identificador.id, "", self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.BOOLEANO:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += "/*Declaracion*/\n"
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = 0;\n'
                    ts.size += 1

                    newSimbolo.SimboloPremitivo(self.identificador.id, False, self.tipo, self.mut, sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return codigo
            else:
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, tipo.UNDEFINED, self.mut,sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

       # print("=== SE DECLARO LA VARIABLES === ", self.identificador.id)
       # print("=== TIPO === ", self.tipo)
       # print("=== Expresion === ", self.expresion)
