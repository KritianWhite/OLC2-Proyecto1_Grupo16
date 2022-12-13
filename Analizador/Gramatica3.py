from AST.TablaErrores import TablaErrores
E_list = TablaErrores()
##
reservadas = {
    'class'     : 'CLASS',
    'local'     : 'LOCAL',
    'int'       : 'TIPOINT',
    'float'     : 'TIPOFLOAT',
    'bool'      : 'TIPOBOOL',
    'str'       : 'TIPOSTRING',
    'char'      : 'TIPOCHAR',
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
             # ** ** ** ** ** OPERACION MATEMATICA ** ** ** ** **
             'SUMA',
             'RESTA',
             'MULTI',
             'DIVI',
             'MODULO',
             # ** ** ** ** ** OPERACION RELACIONAL ** ** ** ** **
             'MENORIGUAL',
             'MAYORIGUAL',
             'IGUALDAD',
             'DESIGUALDAD',
             'MENOR',
             'MAYOR',
             # ** ** ** ** ** OPERACION LOGICA ** ** ** ** **
             'OR',
             'AND',
             'NOT',
             # ** ** ** ** ** SIMBOLOS LENGUAJE ** ** ** ** **
             'LI',
             'LD',
             'CI',
             'CD',
             'PI',
             'PD',
             'PYC',
             'DP',
             'COMA',
             'PUNTO',
             'IGUAL',
             'BARRA',
             'GBAJO',
             'REFER',
             # ********** EXPRESIONES REGUALES **********
             'FLOAT',
             'ENTERO',
             'CADENA',
             'CARACTER',
             'ID',
             'ERR'
         ] + list(reservadas.values())

# Tokens
# ********** OPERACION MATEMATICA **********
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_MODULO = r'%'
# ********** OPERACION RELACIONAL **********
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUALDAD = r'=='
t_DESIGUALDAD = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
# ********** OPERACION LOGICA **********
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
# ********** SIMBOLOS LENGUAJE **********
t_LI = r'\{'
t_LD = r'\}'
t_CI = r'\['
t_CD = r'\]'
t_PI = r'\('
t_PD = r'\)'
t_PYC = r';'
t_DP = r':'
t_COMA = r','
t_PUNTO = r'\.'
t_IGUAL = r'='
t_BARRA = r'\|'
t_GBAJO = r'_'
t_REFER = r'&'

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        print("Se reconcio FLOAT ", t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        print("Se reconcio ENTERO ", t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_Especiales_0(t):
    r'::[a-zA-Z_][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_1(t):
    r'[a-zA-Z][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_2(t):
    r'::[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


def t_Especiales_3(t):
    r'[a-zA-Z][a-zA-Z_0-9]*!'
    return revicion_reservadas(t)


def t_Especiales_4(t):
    r'&[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


# [a-zA-Z_][a-zA-Z_0-9]*
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def revicion_reservadas(t):
    t.type = reservadas.get(t.value, 'ERR')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    print("Se reconcio cadena: ", t.value)
    return t


def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    print("Se reconcio caracter: ", t.value)
    return t


# Comentario simple // ...
def t_COMENTARIO(t):
    r'//.*\n'
    print("Se reconcio comentario: ", t.value.replace('\n', ''))
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t\r"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    E_list.agregar_error("El caracter" + str(t.value[0]) +" no es aceptado por analizador", 0, " Lectura de entrada ", t.lexer.lineno,find_column(t.value, t))
    E_list.print_errores()
    print("Error lexico ", t.value[0])
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MAYORIGUAL', 'MAYOR', 'MENORIGUAL', 'MENOR', 'IGUALDAD', 'DESIGUALDAD'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVI'),
    ('left', 'MODULO'),
    ('right', 'NOT', 'UMENOS')
)

# Definición de la gramática
def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''

    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion  : funcion
                    | declaracion
                    | declaracion_arreglo
                    '''

    t[0] = t[1]


def p_lista_bloque(t):
    ''' lista_bloque : lista_bloque bloque
                    | bloque'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_bloque(t):
    '''bloque : impresiones
                | declaracion
                | asignacion
                | llamada
                | start_if
                | start_while
                | return_ins
                | break_ins
                | continue_ins
                | start_loop
                | declaracion_arreglo
                | start_for
                | funcion_nativa
                | '''

    if len(t) > 1:
        t[0] = t[1]
    else:
        t[0] = None


'''xxx'''
from AST.Expresion import Identificador
from AST.Instruccion import Declaracion, Asignacion, Funcion, Llamada, DeclaracionArreglo,DeclaracionVector
from AST.TablaSimbolos.Tipos import tipo
from AST.Expresion.Nativas import Nativas, NativasVectores
from AST.Expresion.Operaciones import Logica
from AST.Instruccion.Match import Match, BloqueMatch
from AST.Expresion import Primitivo
from AST.Instruccion import Imprimir
from AST.Expresion.Operaciones import Aritmetica, Relacional
from AST.Instruccion.SentenciasControl import Ifs
from AST.Instruccion.SentenciasCiclicas import While,Loop,For
from AST.Instruccion.SentenciasTranferencia import Return,Break,Continue
from AST.Expresion.Arreglo import ArregloData, AccesoArreglo
from AST.Expresion.Casteo import  Casteo
from AST.Expresion.Vector import VectorData
from AST.TablaSimbolos import InstanciaStruct
from AST.Expresion.Struct import AccesoStruct
from AST.Expresion import DeclararStruct, Repeticiones

'''zZz'''


def p_declaracion(t):
    '''declaracion  :   ID tipado
                        |  ID tipado IGUAL expresiones'''

    if len(t) == 3:
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], False)

        '''elif len(t) == 4:
        #este tengo que modificar
        mi_tipo = ""
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), t[3], None, False)'''

    elif len(t) == 5:
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), t[3], t[2], False)


def p_tipado(t):
    '''tipado      : DP tipo_datos
                     |'''
    if len(t) > 1:

        t[0] = t[2]
    else:
        t[0] = None


def p_tipo_datos(t):
    '''tipo_datos     : TIPOINT
                      | TIPOFLOAT
                      | TIPOCHAR
                      | TIPOSTRING
                      | DIRSTRING
                      | TIPOBOOL
                      | TIPOUSIZE
                      | ID'''

def p_expresiones(t):
    '''expresiones  : expre_logica
                    | expre_relacional
                    | expre_aritmetica
                    | datos
                    '''

    t[0] = t[1]

def p_expre_logica(t):
    ''' expre_logica : expresiones OR expresiones
                    | expresiones AND expresiones
                    | NOT  expresiones'''
    if len(t) == 3:
        if t.slice[1].type == 'NOT':
            t[0] = Logica.Logica(t[2], "!", None, True)
    elif len(t) == 4:
        if t.slice[2].type == 'OR':
            t[0] = Logica.Logica(t[1], "||", t[3], False)
        elif t.slice[2].type == 'AND':
            t[0] = Logica.Logica(t[1], "&&", t[3], False)

def p_expre_relacional(t):
    '''expre_relacional : expresiones MAYORIGUAL expresiones
                    | expresiones MAYOR expresiones
                    | expresiones MENORIGUAL expresiones
                    | expresiones MENOR expresiones
                    | expresiones IGUALDAD expresiones
                    | expresiones DESIGUALDAD expresiones'''

    if len(t) == 4:
        if t[2] == ">=":
            t[0] = Relacional.Relacional(t[1], ">=", t[3], False)
        elif t[2] == ">":
            t[0] = Relacional.Relacional(t[1], ">", t[3], False)
        elif t[2] == "<=":
            t[0] = Relacional.Relacional(t[1], "<=", t[3], False)
        elif t[2] == "<":
            t[0] = Relacional.Relacional(t[1], "<", t[3], False)
        elif t[2] == "==":
            t[0] = Relacional.Relacional(t[1], "==", t[3], False)
        elif t[2] == "!=":
            t[0] = Relacional.Relacional(t[1], "!=", t[3], False)

def p_expre_aritmetica(t):
    '''expre_aritmetica : RESTA expresiones %prec UMENOS
                    | PI expresiones PD
                    | expresiones RESTA expresiones
                    | expresiones SUMA expresiones
                    | expresiones MULTI expresiones
                    | expresiones DIVI expresiones
                    | expresiones MODULO expresiones
                    | TIPOFLOAT POWF PI expresiones COMA expresiones PD
                    | TIPOINT POW PI expresiones COMA expresiones PD '''

    if len(t) == 3:
        if t[1] == "-":
            t[0] = Aritmetica.Aritmetica(t[2], "-", 0, True)
    elif len(t) == 4:
        if t[2] == "+":
            t[0] = Aritmetica.Aritmetica(t[1], "+", t[3], False)
        elif t[2] == "-":
            t[0] = Aritmetica.Aritmetica(t[1], "-", t[3], False)
        elif t[2] == "*":
            t[0] = Aritmetica.Aritmetica(t[1], "*", t[3], False)
        elif t[2] == "/":
            t[0] = Aritmetica.Aritmetica(t[1], "/", t[3], False)
        elif t[2] == "%":
            t[0] = Aritmetica.Aritmetica(t[1], "%", t[3], False)
        elif t[1] == "(" and t[3] == ")":
            t[0] = t[2]
    elif len(t) == 8:

        if t[2] == "::pow":
            t[0] = Aritmetica.Aritmetica(t[4], "^", t[6], False)
        elif t[2] == "::powf":
            t[0] = Aritmetica.Aritmetica(t[4], "^f", t[6], False)

def p_datos(t):
    '''datos : ENTERO
            | FLOAT
            | CADENA
            | CARACTER
            | ID
            | TRUE
            | FALSE'''

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo.Primitivo(t[1], 'ENTERO')
    elif t.slice[1].type == 'FLOAT':
        t[0] = Primitivo.Primitivo(t[1], 'DECIMAL')
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo.Primitivo(t[1], 'DIRSTRING')
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo.Primitivo(True, 'BOOLEANO')
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo.Primitivo(False, 'BOOLEANO')
    elif t.slice[1].type == 'CARACTER':
        t[0] = Primitivo.Primitivo(t[1], 'CARACTER')
    elif t.slice[1].type == 'ID':
        t[0] = Identificador.Identificador(t[1])
    else:
        t[0] = Primitivo.Primitivo(t[2], 'DIRSTRING')


def p_error(t):
    try:
        print("\n========================= Error sintáctico en '%s'" % t.value, " =========================")
        E_list.agregar_error("No se esperaba el caracter: " + str(t.value) + ", se ignoro", 1, " Lectura de entrada ",
                             t.lexer.lineno, t.lexer.lexpos)
        E_list.print_errores()
    except:
        print("")

    if t:
        print("Token: ", t, "\n")
        parser.errok()
    else:
        print("Syntax error at EOF")



import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)