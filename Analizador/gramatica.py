from Patron_Interprete.Tabla_Simbolos.Tipos import Tipos
from Patron_Interprete.Expresion.Declaracion import Declaracion
from Patron_Interprete.Expresion.Primitivo import Primitivo
from Patron_Interprete.Expresion.Identificador import Identificador
from Patron_Interprete.Expresion.Operaciones.Aritmeticas import Aritmetica
from Patron_Interprete.Instruccion.Imprimir import Imprimir
from Patron_Interprete.Expresion.Operaciones.Relacional import Relacional

from Patron_Interprete.Controlador import Controlador
from Generador_3D.Generador3D import Generador3D
from Patron_Interprete.Tabla_Simbolos.Tipos import RetornoType


reservadas = {
    'class'     : 'CLASS',
    'local'     : 'LOCAL',
    'int'       : 'INT',
    'float'     : 'FLOAT',
    'bool'      : 'BOOL',
    'string'    : 'STRING',
    'list'      : 'LIST',
    'Struct'    : 'STRUCT',
    'println'   : 'PRINTLN',
    'print'     : 'PRINT',
    'def'       : 'DEF',
    'if'        : 'IF',
    'elif'      : 'ELIF',
    'else'      : 'ELSE',
    'None'      : "NONE",
    'while'     : 'WHILE',
    'for'       : 'FOR',
    'in'        : 'IN',
    'range'     : 'RANGE',
    'break'     : 'BREAK',
    'continue'  : 'CONTINUE',
    'return'    : 'RETURN', 
    'True'      : 'TRUE',
    'False'     : 'FALSE'  
     
}

tokens = [
    
    "LINEANUEVA",
    "DOSP",
    "PUNTO",
    "cadenaString",
    "COMA",
    "LLAVIZQ",
    "LLAVDER",
    "CORCHETEIZQ",
    "CORCHETEDER",
    "PARIZQ",
    "PARDER",
    "IGUAL",
    "MAS",
    "MENOS",
    "POR",
    "DIVIDIDO",
   # "POT",
    "MODULO",
    "MENQUE",
    "MENIGUALQUE",
    "MAYQUE",
    "MAYIGUALQUE",
    "IGUALQUE",
    "NIGUALQUE",
    "DECIMAL",
    "ENTERO",
    "CADENA",
    "ID"
] + list(reservadas.values())

# Tokens
#t_LINEANUEVA = r'\n'
t_DOSP = r':'
t_PUNTO = r'\.'
t_COMA = r','
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r']'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_MAS = r'\+'
t_MENOS = r'-'
#t_POT = r'\*\*'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MODULO = r'%'
t_MENQUE = r'<'
t_MENIGUALQUE = r'<='
t_MAYQUE = r'>'
t_MAYIGUALQUE = r'>='
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='
t_IGUAL = r'='
# Tokens

#TIENE QUE ESTAR EL DOUBLE ANTES SINO DA ERROR
def t_float(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
       # listaMensajes.append(Mensajes(6, "", "", "Valor numerico (Double) <"+t.value+">  incorrecto", t.lexer.lineno, t.lexpos))
        t.value = 0        
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
       # listaMensajes.append(Mensajes(6, "", "", "Valor numerico (Int) <"+t.value+">  incorrecto", t.lexer.lineno, t.lexpos))
        t.value = 0
    return t



def t_cadenaString(t):
    r'"(.|\n|\r|_|\t|\\\'|\\\\)*?"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t



def t_char(t):
    r'\'([^\n\r\\]|[a-zA-Z0-9]|\\n|\\N|\\r|\\R|\\t|\\T|\\"|\\\'|\\\\)\''
    t.value = t.value[1:-1] # removes apostrophe
    t.value = t.value.replace('\\\\','\\')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\N','\n')
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\T','\t')
    t.value = t.value.replace('\\r','\r')
    t.value = t.value.replace('\\R','\r')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace('\\\'','\'')
    t.value = t.value.lower()
    return t

    
t_ignore = " \t\r"

def find_column(inp, token):
   # line_start = inp.rfind('\n', 0, token.lexpos) + 1
   # return (token.lexpos - line_start) + 1
    return 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    #listaMensajes.append(
   # Error("Léxico", "Caracter invalido '%s'" % t.value[0], 0, 0))
    t.lexer.skip(1)

    




import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia

precedence = (
    #('left', 'OR'),
    #('left', 'AND'),
    ('left', 'IGUALQUE', 'NIGUALQUE'),
    ('left', 'MAYQUE', 'MENQUE', 'MAYIGUALQUE', 'MENIGUALQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO')
    #('left', 'POT'),
    #('right', 'UMENOS')
)


# Definición de la gramática



def p_init(t):
    'init : linstrucciones'
    t[0] = t[1]


def p_linstrucciones(t):
    'linstrucciones : linstrucciones instrucciones'
    t[1].append(t[2])
    t[0] = t[1]

def p_linstrucciones2(t):
    'linstrucciones : instrucciones'
    t[0] = [t[1]]

def p_instrucciones(t):
    '''instrucciones :  asignacion
                    | imprimir
                    | imprimirln
                    | exp
                
                     ''' 
    t[0] = t[1]

def p_funcNativas(t):
    '''funciones_nativas : imprimir'''
    t[0]    =   t[1]

# DECLARACION :
#Declaracion normal
def p_asignacion1(t):
    'asignacion :  lista_ID IGUAL  exp '
    t[0] = Declaracion(t.lineno(1), find_column(input, t.slice[1]), str(t[1]),None, t[3], False)
     #(self,fila,columna,identificador, tipo, expresion=None,es_mutable=False

#Declaracion con tipo
def p_asignacion2(t):
    'asignacion :  lista_ID IGUAL  exp DOSP tipo '
    t[0] = Declaracion(t.lineno(1), find_column(input, t.slice[1]), str(t[1]),t[5], t[3], False)
     #(self,fila,columna,identificador, tipo, expresion=None,es_mutable=False

def p_listaParametros(t):
    'lista_ID : lista_ID COMA ID'
    t[1].append(t[3])
    t[0] = t[1]
     
def p_listaParametros2(t):
    'lista_ID : ID'
    t[0] = [t[1]]

def p_imprimir(t):
    'imprimir : PRINT PARIZQ impresiones PARDER'
    t[0] = Imprimir(t.lineno(1), find_column(input, t.slice[1]), t[3])
    

def p_imprimirln(t):
    'imprimirln : PRINTLN PARIZQ impresiones PARDER'
    t[0] = Imprimir(t.lineno(1), find_column(input, t.slice[1]), t[3])
    # println(“+”, “-”); 

def p_impresiones(t):
    'impresiones : impresiones COMA prima_impresiones '
    t[1].append(t[3])
    t[0] = t[1]

def p_impresiones2(t):
    ' impresiones : prima_impresiones '
    t[0] = [t[1]]
    
def p_primaImpresiones(t):
    ''' prima_impresiones : ID 
                            | exp '''
    t[0] = t[1]



def p_tipo(t):
    '''tipo : INT 
        | BOOL
        | FLOAT
        | STRING
        | NONE
        |
        '''
    #print(str(Tipo.getTipo(str(t[1]))))
    if str(t[1]).lower()== "int":
        t[0]= Tipos.ENTERO
    elif str((t[1])).lower() == "float":
        t[0]= Tipos.DOBLE
    elif str((t[1])).lower() == "bool": 
        t[0]= Tipos.BOOLEANO
    elif str((t[1])) == "string":
       # print("reconocio string ")
        t[0]= Tipos.STRING


def p_exp(t):
    'exp : INT'
   
    t[0] = Primitivo(t.lineno(1), find_column(
       input, t.slice[1]), Tipos.ENTERO, int(t[1]))

def p_exp2(t):
    'exp : FLOAT'
 
    t[0] = Primitivo(t.lineno(1), find_column(
        input, t.slice[1]), Tipos.DOBLE,float(t[1]))

def p_expTrue(t):
    'exp : TRUE'
    t[0] =  Primitivo(t.lineno(1), find_column(input, t.slice[1]), Tipos.BOOLEANO, True)

def p_expFalse(t):
    'exp : FALSE'
    t[0] =  Primitivo(t.lineno(1), find_column(input, t.slice[1]), Tipos.BOOLEANO, False)

 


   

def  p_exp7(t):
    'exp : cadenaString'
    print("reconoce cadena")
    t[0] = Primitivo(t.lineno(1),find_column(input, t.slice[1]), Tipos.STR ,str(t[1]))    
    
def p_exp8(t):
    'exp : PARIZQ exp PARDER'
    t[0] = t[2]

def p_exp9(t):
    'exp : ID'
    t[0] = Identificador(t.lineno(1),find_column(input, t.slice[1]), str(t[1]) )


def p_exp10(t):
    ''' exp : exp MAS exp
    | exp MENOS exp
    | exp DIVIDIDO exp
    | exp POR exp
    | exp MODULO exp
    
    
    '''
    t[0] = Aritmetica(t[1],t[3],str(t[2]),t.lineno(1),find_column(input, t.slice[1]))


#def p_exp12(t):
#    'exp : sent_loop'
#    t[0] = t[1]

# def p_logicas(t):
#     ''' exp : exp OR exp
#     | exp AND exp
#     '''
#     t[0] = Logicas(str(t[2]) , t.lineno(1),find_column(input, t.slice[1]), t[1] , t[3]  )

# def p_logicas2(t):
#     ''' exp : NOT exp 
#     '''
#     t[0] = Logicas(str(t[1]) , t.lineno(1),find_column(input, t.slice[1]), t[2]  )

def p_relacionales3(t):
    '''exp : exp MAYQUE exp  
    | exp MENIGUALQUE exp
    | exp MAYIGUALQUE exp
    | exp MENQUE exp
    | exp IGUALQUE exp
    | exp NIGUALQUE exp
    
    '''
    t[0] = Relacional(t[1] , str(t[2]),t[3], False)
    #(self,fila,columna, operador, expresion_1,expresion_2)









def p_error(t):
    print(f'Error sintáctico en { t.value!r}')

import ply.yacc as yacc

parser = yacc.yacc()
listaMensajes = []

           


def analizar(data):
    global listaMensajes
    listaMensajes.clear()
    instrucciones = parser.parse(data)
    entornoGlobal = Generador3D(None)
    manejadorGlobal = Controlador()

    for ins in instrucciones:
           valor = ins.traducir(entornoGlobal,manejadorGlobal)

    cod = manejadorGlobal.codigo
   

    tablaGlobal : RetornoType =entornoGlobal.getTablaSimbolosC3DS()

    
   
 
    for simbolo in tablaGlobal:
        sim =tablaGlobal[simbolo]
        
    
        print( sim.nombre)
        print(sim.tipo)
        print(sim.tipo_declaracion)
        print("\n")
    
    
    
    print("************************************************")
    return manejadorGlobal
