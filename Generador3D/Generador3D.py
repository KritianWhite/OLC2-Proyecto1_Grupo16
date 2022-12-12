
class Generador3D:
    def __init__(self):
        self.temporales =0
        self.etiquetas =0
        self.codigo = ""
        self.main = ""
        self.funciones = ""
        self.listafunciones = []
        self.listareturn = []

    def obtenerTemporal(self):
        #retorna cadena
        temp = "t"+str(self.temporales)
        self.temporales +=1
        return temp

    def addIntruccion(self,codigo):
        self.codigo += codigo + '\n'

    def obtenerEtiqueta(self):
        et = "L"+str(self.etiquetas)
        self.etiquetas += 1
        return et

    def agregarReturn(self,nombre):
        self.listareturn.append(nombre)
## se modifica encabezado para go
    def generarEncabezado(self):
        encabezado = ""
        encabezado += """
package main

import ("fmt")

var SP, HP float64;
var Stack [30101999]float64;
var Heap [30101999]float64;
\n"""
        if self.temporales > 0:   ## se modifica la manera para declarar las variables temporales
            encabezado += "var "
        for i in range(0, self.temporales):
            if i % 15 == 0 and i > 0:
                encabezado += "\n"
            encabezado += f"t{i}"
            if i < self.temporales - 1:
                encabezado += ","

        if self.temporales > 0:
            encabezado += " float64; \n\n"

        if len(self.listareturn) > 0:
            encabezado += "var "
            for i in range(0, len(self.listareturn)):
                if i == len(self.listareturn) - 1:
                    encabezado += self.listareturn[i]
                else:
                    encabezado += self.listareturn[i] + ","
            encabezado += " float64; \n\n"

        return encabezado

    def agregarInstruccion(self, codigo):
        self.main += codigo + '\n'
        print(self.main)

        ##elimina return 0 go no lo lleva \treturn 0;
    def generarMain(self):
        codigo_SALIDA = self.generarEncabezado()
        codigo_SALIDA += self.codigo + '\n'
        codigo_SALIDA += self.declararfuciones() + "\n\n\n"
        codigo_SALIDA += self.funciones
        codigo_SALIDA += 'func main()' + "{\n SP = 0\n HP = 0\n " + f'\n {self.main}  \n' + "}"

        return codigo_SALIDA

    def declararfuciones(self):
        codigo = ""
        for x in self.listafunciones:
            codigo += f'void {x}();\n'
        return  codigo

    def FuncionEjecutado(self,identificador):
        validacion = False
        for x in self.listafunciones:
            if x == identificador:
                validacion = True
        return validacion

    def agregaridfuncion(self,identificador):
        self.listafunciones.append(identificador)

    def agregarFuncion(self, codigo,identificador):
        self.funciones += f'void {identificador}()'
        self.funciones += "{\n"
        self.funciones += codigo+"\n"
        self.funciones += "return;\n}"
        self.funciones += "\n\n\n"

    def reiniciarGenerador(self):
        self.etiquetas =0
        self.codigo = ""
        self.temporales = 0
        self.funciones = ""
        self.main = ""
