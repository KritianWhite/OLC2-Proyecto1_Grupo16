from Patron_Interprete.Abstracto.Expresion import Expresion
from Patron_Interprete.Expresion.Operaciones.Operacion import Operacion, operador
from Patron_Interprete.Tabla_Simbolos.Tipos import tipo as t
from Patron_Interprete.Tabla_Simbolos.Tipos import RetornoType

class Relacional(Operacion, Expresion):

    def __init__(self, exp1, signo, exp2, expU):
        super().__init__(exp1, signo, exp2, expU)
        self.etiquetaV = ""
        self.etiquetaF = ""

    def Obtener3D(self, controlador, ts):
        return_exp1:RetornoType = self.exp1.Obtener3D(controlador, ts)
        return_exp2:RetornoType = self.exp2.Obtener3D(controlador, ts)

        #valor_exp1 = return_exp1.valor
        #valor_exp2 = return_exp2.valor

        tipo_exp1 = return_exp1.tipo
        tipo_exp2 = return_exp2.tipo

        codigo = ""

        if self.operador == operador.MAYORIGUAL:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} >= {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo, "", "", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

        elif self.operador == operador.MAYORQUE:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} > {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo,"","", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

        elif self.operador == operador.MENORIGUAL:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} <= {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo, "", "", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

        elif self.operador == operador.MENORQUE:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} < {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo, "", "", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

        elif self.operador == operador.IGUALIGUAL:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} == {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo, "", "", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

        elif self.operador == operador.DIFERENCIA:
            codigo += return_exp1.codigo + "\n"
            codigo += return_exp2.codigo + "\n"
            codigo += f'\tif ({return_exp1.temporal} != {return_exp2.temporal}) goto {self.etiquetaV};\n'
            codigo += f'\tgoto {self.etiquetaF};\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo, "", "", t.BOOLEANO)
            retorno.etiquetaV = self.etiquetaV
            retorno.etiquetaF = self.etiquetaF
            return retorno

