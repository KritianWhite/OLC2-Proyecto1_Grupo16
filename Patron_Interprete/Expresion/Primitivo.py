from Patron_Interprete.Abstracto.Expresion import Expresion
from Patron_Interprete.Tabla_Simbolos.Tipos import Tipos, RetornoType
from Patron_Interprete.Tabla_Simbolos.Tipos import tipo as ttipo


class Primitivo(Expresion):

    def __init__(self, fila, columna, tipo, valor) :
        self.valor = valor
        self.tipo = Tipos(tipo)
        self.etiquetaV = ""
        self.etiquetaF = ""
        self.fila = fila
        self.columna = columna

    def Obtener3D(self, controlador, ts) -> RetornoType:

        temp = None
        codigo = ""
        retorno = RetornoType(self.valor)

        if self.tipo.tipo == ttipo.ENTERO or self.tipo.tipo or  self.tipo.tipo == ttipo.DECIMAL:
            temp = controlador.Generador3D.obtenerTemporal()
            codigo = f'\t{temp} = {self.valor};'

        elif self.tipo.tipo == ttipo.BOOLEANO:
            temp = controlador.Generador3D.obtenerTemporal()

            if self.etiquetaV != "" and self.valor == True:
                codigo += f"goto {self.etiquetaV};\n"
                retorno.etiquetaV = self.etiquetaV
                retorno.etiquetaF = self.etiquetaF

            elif self.etiquetaF != "" and self.valor == False:
                codigo += f"goto {self.etiquetaF};\n"
                retorno.etiquetaV = self.etiquetaV
                retorno.etiquetaF = self.etiquetaF

            else:
                if self.valor:
                    codigo = f'\t{temp} = 1;'
                else:
                    codigo = f'\t{temp} = 0;'

        elif self.tipo.tipo != ttipo.STRING or self.tipo.tipo != ttipo.DIRSTRING or self.tipo.tipo != ttipo.CARACTER:

            temp = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp} = HP;\n'

            estado = 0
            for caracter in self.valor:

                if caracter == '\\' and estado == 0:
                    estado = 1
                    continue

                if estado == 1:
                    if caracter == 'n':
                        codigo += f'\tHeap[HP] = 10;\n'
                        codigo += f'\tHP = HP +1;\n'
                        estado = 0
                        continue

                codigo += f'\tHeap[HP] = {ord(caracter)};\n'
                codigo += f'\tHP = HP +1;\n'

            codigo += f'\tHeap[HP] = 0;\n'
            codigo += f'\tHP = HP +1;\n'


        retorno.iniciarRetorno(codigo,None,temp,self.tipo.tipo)
        return retorno



