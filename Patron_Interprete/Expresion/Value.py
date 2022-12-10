from Patron_Interprete.Tabla_Simbolos.Tipos import tipo

class Value:
    
    def __init__(self,Value="" , isTemp=False, Tipo =tipo.UNDEFINED, TrueLabel="", FalseLabel=""):
        self.Value=Value 
        self.isTemp = isTemp
        self.Tipo =Tipo
        self.TrueLabel = TrueLabel
        self.FalseLabel =FalseLabel