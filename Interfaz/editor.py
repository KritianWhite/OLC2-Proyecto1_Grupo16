import tkinter
import sys
sys.setrecursionlimit(5000)
from tkinter import scrolledtext as st

#CREANDO VENTANA DEL EDITOR
ventana = tkinter.Tk()

ventana.geometry("1320x700")
ventana.title("Proyecto1 OLC2")



def contLineasEjecutar():
    cont = 0
    texto = ""
    while(cont != 100):
        texto = texto + str(cont) + "\n"
        cont = cont + 1
    tk_line_counter.insert("1.0", texto)


def cargaMensajes(ListaMensajes):
    clearTextOutPut()
    msj = ""
    for m in ListaMensajes:
        msj += m.getMensaje() + "\n"
        #print(m.getMensaje())
    tk_text_Output.insert("1.0", msj)

def clearTextOutPut():
    tk_text_Output.delete("1.0","end")
    tk_text_OutputError.delete("1.0","end")

def readFile():
    nameFile = "entrada.txt"
    #limpiar entrada de texto
    tk_text_input.delete("1.0","end")
    #open file
    f = open(nameFile,'r',encoding='utf-8')
    textInput = f.read()
    f.close()
    #insertar texto en la caja de texto
    tk_text_input.insert("1.0", textInput)
    #asignando el contador de lineas
    contadorDeLineasAlCargarArchivo(nameFile)

def contadorDeLineasAlCargarArchivo(nameFile):
    #limpiamos
    countLines = 0
    lineCounter = "0"
    tk_line_counter.delete("1.0","end")
    #leemos archivo
    f2 = open(nameFile,'r',encoding='utf-8')
    for line in f2:
        if countLines != 0:
            lineCounter = lineCounter + "\n" +str(countLines)
        countLines = countLines + 1

    f2.close()
    #insertamos texto en caja de texto
    tk_line_counter.insert("1.0", lineCounter)

def main():
    #capturando texto de la caja de texto
    data = str(tk_text_input.get("1.0",tkinter.END+"-1c"))
 
    #Caracteres especiales
    data = data.replace('\\\\','\\')
    data = data.replace('\\n','\n')
    data = data.replace('\\N','\n')
    data = data.replace('\\t','\t')
    data = data.replace('\\T','\t')
    data = data.replace('\\r','\r')
    data = data.replace('\\R','\r')
    data = data.replace('\\"','\"')
    data = data.replace('\\\'','\'')
    data = data.lower()
    manejador_final  = gramatica.analizar(data)
    listaMensajes = manejador_final.codigo
    salida = ""
    salidaError = ""
    contador_Salida = 0
    contador_Error = 0
    """
    for m in listaMensajes:
        if m.tipo == 5:
            salida = salida + m.getMensaje() +"\n"
            contador_Salida = contador_Salida + 1
        else:
            outPutError = outPutError  + str(contError) + ") "+ msj.getMensaje() + "\n"
            contError = contError + 1
    """
    salida = salida + manejador_final.cabecera()
    for i in listaMensajes:
        salida = salida + i+"\n"

    clearTextOutPut()
    tk_text_Output.insert("1.0", salida)
    tk_text_OutputError.insert("1.0", outPutError)
    contLineasEjecutar()
    ReporteErroresHtml(listaMensajes)
         




x_btn = 125
y_btn = 380


#CREANDO LA CONSOLA DE ENTRADA
tk_text_input = tkinter.Text(ventana, height=20,width = 170)
tk_text_input.place(x=55,y=10)
#PARA CONTAR LAS LINEAS
tk_line_counter = tkinter.Text(ventana,height=20,width = 5)
tk_line_counter.place(x=10,y=10)

#BOTON PARA CARGAR ARCHIVOS
btnOpenFile = tkinter.Button(ventana,text="Cargar Archivo",bg="#00ff9c",command = readFile)
btnOpenFile.place(x= x_btn+30,y=y_btn)

#boton princial, tendra la ejecucion del analizador lexico, sintactico y semantico
btnExecute = tkinter.Button(ventana,text="Ejecutar", command=main ,bg="#1E90FF")
btnExecute.place(x= x_btn+280,y=y_btn)

#CONSOLA DE SALIDA 

tk_text_Output = tkinter.Text(ventana, height = 15, width = 90)
tk_text_Output.place(x = 55, y = y_btn +50)





tk_text_OutputError = tkinter.Text(ventana,height = 15 , width = 80)
tk_text_OutputError.place(x = 700, y = y_btn + 50 )

ventana.mainloop()