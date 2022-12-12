from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Analizador.gramatica as g
from AST.AST_Ejecucion.AST import AST
from AST.Controlador import Controlador
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
import io
import webbrowser
import os
from AST.TablaErrores import TablaErrores
opcion = ["No data"]

def ventanas():

        global opcion

        ventana = Tk()
        ventana.title('Proyecto1 OLC2')
        ventana.geometry("1600x900")

        def cerrar():
            exit()

        def Run_code():
            g.E_list.reiniciar()
            ConsoleTxt.configure(state='normal')
            ConsoleTxt.delete('1.0', END)
            ConsoleTxt.configure(state='disabled')

            #f = io.open("../Analizador/entrada.txt", mode="r", encoding="utf-8")
            #entrada = f.read()
            #instrucciones = g.parse(entrada)

            CodeText = CodeTxt.get("1.0", 'end-1c')
            instrucciones = g.parse(CodeText)

            ts = TablaDeSimbolos(None,"Main")
            controlador= Controlador()
            AST_ej = AST(instrucciones)

            consola = AST_ej.Ejecutar3D(controlador, ts)
            #print(consola)

            ConsoleTxt.configure(state='normal')
            ConsoleTxt.insert("1.0",consola)
            ConsoleTxt.configure(state='disabled')


        notebook = ttk.Notebook(ventana)
        notebook.pack(fill=BOTH, expand=1)

        s = ttk.Style()
        s.configure('TFrame', background='#1e81b0')

        pes1 = ttk.Frame(notebook)

        notebook.add(pes1, text='')

        Button(pes1, width="8", height="2", text="Salir", background="#e28743", command=cerrar).place(x=1490, y=800)

        Label(pes1, text="Consola de entrada:", font=("Popins", 12)).place(x=30, y=95)

        Label(pes1, text="Consola de salida:",  font=("Popins", 12)).place(x=800, y=95)

        CodeTxt = Text(pes1, width=94, height=40)
        CodeTxt.grid(row=1, column=0)
        CodeTxt.place(x=30,y=120)

        ConsoleTxt = Text(pes1, width=94, height=40)
        ConsoleTxt.grid(row=1, column=0)
        ConsoleTxt.place(x = 800, y=120)
        ConsoleTxt.configure(state='disabled')

        Button(pes1, width="6", height="2", text="RUN", background="#22823b", command=Run_code).place(x=1500, y=30)

        def Open_TablaSimbolos():
            filename = '../Reportes/TablaSimbolos.HTML'
            webbrowser.open('file://' + os.path.realpath(filename))

        Button(pes1, text="Tabla de simbolos", command=Open_TablaSimbolos).place(x=30, y=30)

        def Open_TablaErrores():
            filename = '../Reportes/TablaErrores.HTML'
            webbrowser.open('file://' + os.path.realpath(filename))

        Button(pes1, text="Tabla de errores", command=Open_TablaErrores).place(x=150, y=30)

        def Open_TablaErrore():
            Consoletexet = ConsoleTxt.get("1.0", 'end-1c')
            AST_ej = AST([])
            AST_ej.Optimizacion(Consoletexet)

           #filename = '../Reportes/Tabla.HTML'
            #webbrowser.open('file://' + os.path.realpath(filename))

        Button(pes1, text="Opt. codigo", command=Open_TablaErrore).place(x=270, y=30)
        # Terminar ------------------------------------------------------------------------------------

        ventana.mainloop()

if __name__ == "__main__":

    ventanas()
