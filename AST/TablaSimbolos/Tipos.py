from enum import Enum


class tipo(Enum):
    ENTERO = 0,
    DECIMAL = 1,
    BOOLEANO = 2,
    CARACTER = 3,
    STRING = 4,
    UNDEFINED = 5,
    RETURN = 6,
    BREAK = 7,
    CONTINUE = 8,
    ARRAY = 9,
    OBJETO = 10,
    USIZE = 11,
    VECTOR = 12,
    STRUCT = 13,
    ERROR = 14

class RetornoType():
    def __init__(self,  valor = None , tipo = tipo.UNDEFINED , final = tipo.UNDEFINED):
        self.tipo = tipo
        self.valor = valor
        self.final = final

        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.etiquetaV = ""
        self.etiquetaF = ""

        self.codigotemp= ""
        self.codigotempOtros = ""
        self.dimensiones = []

        self.diccionario = None

        self.Objeto = None
        self.valoresObjeto = []

        self.NombreStruck = None

    def iniciarRetorno(self,codigo, etiqueta, temporal,tipo):
        self.codigo = codigo
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo

    def iniciarRetornoArreglo(self,codigo,codigotemp, etiqueta, temporal,tipo, codigotempOtros,dimensiones):
        self.codigo = codigo
        self.codigotemp =codigotemp
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo
        self.codigotempOtros = codigotempOtros
        self.dimensiones = dimensiones



class Tipos():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = self.ObtenerTipo()

    def ObtenerTipo(self):
        if self.nombre == 'ENTERO':
            print("Se dectecto un entero")
            return tipo.ENTERO

        elif self.nombre == 'DECIMAL':
            print("Se dectecto un decimal")
            return tipo.DECIMAL

        elif self.nombre == 'STRING':
            print("Se dectecto una STRING")
            return tipo.STRING

        elif self.nombre == 'CARACTER':
            print("Se dectecto una CARACTER")
            return tipo.CARACTER

        elif self.nombre == 'BOOLEANO':
            print("Se dectecto un booleano")
            return tipo.BOOLEANO

        elif self.nombre == 'USIZE':
            print("Se dectecto un USIZE")
            return tipo.USIZE


        else:
            return tipo.ERROR
