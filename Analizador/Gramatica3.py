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
    'False'     : 'FALSE',
    'len()'       : 'LEN',
    'push': 'PUSH',
    'remove': 'REMOVE',
    'contains': 'CONTAINS',
    'insert' : 'INSERT'
}

tokens = [
             # ** ** ** ** ** OPERACION MATEMATICA ** ** ** ** **
             'SUMA',
             'RESTA',
             'MULTI',
             'DIVI',
             'MODULO',
             'POT',
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
t_POT = r'\*\*'
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
                    | asignacion
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
                | start_while
                | break_ins
                | start_if
                | start_for
                | llamada
                | return_ins
                | asignacion
                | asignacion_arreglo
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

def p_funciones(t):
    '''funcion  : LI lista_bloque LD
                | DEF ID PI parametros  PD  LI lista_bloque LD
                | DEF ID PI parametros PD tipo_datos LI lista_bloque LD
                '''
    if len(t) == 4:
        t[0] = Funcion.Funcion("main", None, [], t[2])
        #t[0] = Funcion.Funcion(t[2], None, [], t[6])
    elif len(t) == 9:
        t[0] = Funcion.Funcion(t[2], None, t[4], t[7])
    elif len(t) == 10:
        t[0] = Funcion.Funcion(t[2], t[6], t[4], t[8])

def p_parametros(t):
    '''parametros : parametros COMA definiciones
                  | definiciones'''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_definiciones(t):
    """ definiciones :  ID tipado
                     """


    print("Llego a definiciones, ",len(t))

    if len(t) == 4:
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[2]), None, t[3],True)

    elif len(t) == 3:
        if t.slice[2].type == 'tipado':
            t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], False)
        else:
            t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], True,True)



def p_instruccion_imprimir(t):
    '''impresiones     : PRINTLN PI  impresion_valores PD
                       | PRINT PI impresion_valores PD '''
    if len(t) == 5:


        if t[1] == 'println':
            t[0] = Imprimir.Imprimir("{}", True, t[3])
            # print("\nRe reocnocio: println! con el token: ", t[3], "\n")
        elif t[1] == 'print':
            t[0] = Imprimir.Imprimir("{}", False, t[3])
            # print("\nRe reocnocio: print! con el token: ", t[3], "\n")

    else:

        if t[1] == 'println':
            t[0] = Imprimir.Imprimir(t[3], True, t[5])
            # print("\nRe reocnocio: println! con el token: ", t[5], "\n")

        elif t[1] == 'print':
            t[0] = Imprimir.Imprimir(t[3], False, t[5])
            # print("\nRe reocnocio: print! con el token: ", t[5], "\n")

def p_imprimir_lista_valores(t):
    '''impresion_valores     :  impresion_valores COMA expresiones
                         | expresiones '''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]


def p_declaracion(t):
    #el primero es para asignar con el nombre de un ide
    '''declaracion  : ID tipado
                        | ID  IGUAL expresiones
                        | ID tipado IGUAL expresiones'''
    #(id: Identificador, expresion, tipo, mut,referencia = False):
    #if len(t) == 2:
    #    t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), "", tipo.UNDEFINED, False)
    if len(t) == 3:
        #esto es para el primero
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], False)

    elif len(t) == 4:
        #este tengo que modificar
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), t[3], None, False)
    elif len(t) == 5:
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), t[4], t[2], False)

def p_lista_Variables(t):
    '''lista_Variables : lista_Variables COMA ID
                        | ID'''
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
def p_start_if(t):

    '''start_if : IF expresiones DP LI list_exp_ins LD
                | IF expresiones DP  LI list_exp_ins LD ELSE DP   LI list_exp_ins LD
                | IF expresiones DP LI list_exp_ins LD lista_elif
                | IF expresiones DP LI list_exp_ins LD lista_elif ELSE DP  LI list_exp_ins LD  '''

    print('Llego if gramatica ', len(t))
    if len(t) == 7:
        t[0] = Ifs.Ifs(t[2],t[5],None,None)
    elif len(t) == 12:
        t[0] = Ifs.Ifs(t[2], t[5], t[10],None)
    if len(t) == 8:
        t[0]= Ifs.Ifs(t[2],t[5],None,t[7])
    if len(t) == 13:
        t[0]= Ifs.Ifs(t[2],t[5],t[11],t[7])


def p_lista_if(t):
    ''' lista_elif : lista_elif else_if
                    | else_if'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]


def p_else_if(t):
    ''' else_if : ELIF  expresiones DP LI list_exp_ins LD '''
    t[0] = Ifs.Ifs(t[2], t[5], None,None)


def p_list_exp_ins(t):
    '''list_exp_ins : list_exp_ins bloque_exp
                | bloque_exp '''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]
def p_return_ins(t):
    '''return_ins : RETURN
                    | RETURN expresiones'''
    if len(t) == 2:
        t[0] = Return.Return(None)
    else:
        t[0] = Return.Return(t[2])

def p_asignacion(t):
    '''asignacion  : ID IGUAL expresiones
                        '''
    t[0] = Asignacion.Asignacion(t[1], t[3])

def p_bloque_exp(t):
    ''' bloque_exp : bloque
                    | expresiones  '''
    t[0] = t[1]

def p_llamada(t):
    '''llamada  : ID PI PD
                | ID PI lista_expres PD'''

    if len(t) == 4:
        print("=== llamda tipo 1")
        t[0] = Llamada.Llamada(t[1], [])
    else:
        print("=== llamda tipo 2")
        t[0] = Llamada.Llamada(t[1], t[3])

def p_lista_expres(t):
    '''lista_expres : lista_expres COMA  expresiones
                    | expresiones '''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]



def p_start_while(t):
    '''start_while : WHILE expresiones LI lista_bloque LD '''
    t[0] = While.While(t[2],t[4])

def p_start_for(t):
    '''start_for : FOR ID IN opciones_for LI lista_bloque LD '''

    t[0]= For.For(t[2],t[4],t[6])

def p_opciones_for(t):
    '''opciones_for :  expresiones
                    | RANGE  PI expresiones PD '''

    if len(t) == 2:
        t[0]= [1,t[1]]
    else:
        t[0]= [2,1,t[3]]




def p_asignacion_arreglo(t):
    ''' asignacion_arreglo : acceso_arreglo IGUAL expresiones '''
    t[1].valor = t[3]
    t[0] = t[1]

def p_acceso_arreglo(t):
    '''acceso_arreglo : ID dimensiones '''
    print("Deberia ser id: ", t[1], " dimensiones: ",t[2])
    t[0] = AccesoArreglo.AccesoArreglo(t[1], t[2])

def p_dimensiones(t):
    '''dimensiones : dimensiones dimension
                    | dimension'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_dimension(t):
    '''dimension : CI expresiones CD  '''
    t[0] = t[2]




def p_tipado(t):
    '''tipado      : DP tipo_datos
                    | '''
    if len(t) > 1:

        t[0] = t[2]
    else:
        t[0] = None


def p_tipo_datos(t):
    '''tipo_datos     : TIPOINT
                      | TIPOFLOAT
                      | TIPOCHAR
                      | TIPOSTRING
                      | TIPOBOOL
                      | ID'''
    if t[1] == "int":
        t[0] = tipo.ENTERO
    elif t[1] == "float":
        t[0] = tipo.DECIMAL
    elif t[1] == "char":
        t[0] = tipo.CARACTER
    elif t[1] == "str":
        t[0] = tipo.STRING
    elif t[1] == "bool":
        t[0] = tipo.BOOLEANO
    else:
        t[0] = Identificador.Identificador(t[1])

def p_break_ins(t):
    '''break_ins : BREAK
                    | BREAK expresiones'''
    if len(t) == 2:
        t[0] = Break.Break(None)
    else:
        t[0] = Break.Break(t[2])

def p_expresiones(t):
    '''expresiones  : funcion_nativa
                    | expre_logica
                    | expre_relacional
                    | expre_aritmetica
                    | expre_valor
                    '''

    t[0] = t[1]

def p_funcion_nativa(t):
    '''funcion_nativa : expresiones PUNTO nativas'''
    #
    print("Llego a nativas")

    if isinstance(t[3],NativasVectores.NativasVectores):
        nativa = t[3]
        nativa.expresion = t[1]
        print("Llego a nativa vectores", nativa)
        t[0] = nativa

    elif  isinstance(t[3],AccesoStruct.AccesoStruct):
        print(t[3])
        print(t[1])
        t[3].identificador = t[1]
        t[0]= t[3]
    else:

        t[0] = Nativas.Nativas(t[1], t[3])

def p_nativas(t):
    '''nativas      :  LEN
                    | nativas_vectores '''
    if len(t) == 5:
        t[0] = NativasVectores.NativasVectores(t[2], t[1].lower())
    else:
        t[0] = t[1]

def p_nativas_vectores(t):
    '''nativas_vectores : PUSH PI expresiones PD
                        | REMOVE PI expresiones PD
                        | CONTAINS PI expresiones PD
                        | INSERT PI expresiones COMA expresiones PD'''

    if len(t)==5:
        t [0] = NativasVectores.NativasVectores(t[3],t[1].lower())
    elif len(t) == 7:
        t[0] = NativasVectores.NativasVectores(t[3], t[1].lower(),t[5])


def p_expre_valor(t):
    '''expre_valor :  start_if
                    | datos
                    | arreglo_init
                    | acceso_arreglo
                    | llamada
                    | datos_cast
                    '''
    t[0] = t[1]



def p_datos_cast(t):
    ''' datos_cast : datos
                  | tipo_datos PI expresiones PD '''

    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0]= Casteo.Casteo(t[3],t[1])


def p_arreglo_init(t):
    '''arreglo_init : CI lista_Expresiones CD '''
    t[0] = ArregloData.ArregloData(t[2])


def p_lista_expresiones(t):
    '''lista_Expresiones : lista_Expresiones COMA expresiones
                        | expresiones'''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]


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
                    | expresiones MODULO expresiones '''

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
        t[0] = Primitivo.Primitivo(t[1], 'STRING')
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo.Primitivo(True, 'BOOLEANO')
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo.Primitivo(False, 'BOOLEANO')
    elif t.slice[1].type == 'CARACTER':
        t[0] = Primitivo.Primitivo(t[1], 'CARACTER')
    elif t.slice[1].type == 'ID':
        t[0] = Identificador.Identificador(t[1])
    else:
        t[0] = Primitivo.Primitivo(t[2], 'STRING')


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