from Patron_Interprete.Tabla_Simbolos.Simbolos import Simbolos

class Entorno:
    
    #constructor con la tabla de simbolos anterior y la nueva 
    def __init__(self, anterior= None):
        self.anterior = anterior
        self.tablaSimbolos = {}
        #size para saber en que posicion de la pila estoy

    def nuevoSimbolo(self, simbolo : Simbolos):
        s= self.tablaSimbolos.get(simbolo.nombre)

        if s == None:
            self.tablaSimbolos[simbolo.nombre] = simbolo
            return "simbolo agregado"

        return "ya existe un simbolo con ese id"

    #para editar el valor de un simbolo
    def editarSimbolo(self, llave, nuevo : Simbolos):
        s=self.tablaSimbolos.get(llave)

        if s != None:
            self.tablaSimbolos[llave] =nuevo
            return "se ha editado con exito el simbolo" + llave
        return "No existe simbolo con llave" + llave
        
    def buscarSimbolo(self, id):
        reco = self

        while reco !=None:
            s = reco.tablaSimbolos.get(id)
            if s !=None:
                return s
            reco = reco.anterior
        
        return None

    def getTablaSimbolos(self):
        return self.tablaSimbolos