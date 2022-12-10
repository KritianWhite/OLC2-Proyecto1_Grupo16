from Patron_Interprete.Abstracto.Instruccion import Intruccion

class Imprimir(Intruccion):
    def __init__ (self , fila , columna, expresion):
        self.fila= fila
        self.columna = columna
        self.expresion = expresion

    def ejecutar(self, entorno, listaMensajes):
        valor=self.expresion.ejecutar(entorno,listaMensajes)
        #print("esta ejecutando imprimir")
        
        #print(valor)
        #print("--------------")
        #listaMensajes.append(Mensajes(5, "","",str(valor),self.fila,self.columna))

    def traducir(self, entorno, manejador):
        print("traducir print")