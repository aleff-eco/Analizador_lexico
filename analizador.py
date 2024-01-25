import ply.lex as lex

# Lista de palabras reservadas
reservadas = ['VAR', 'IF', 'FOR', 'DEF', 'IN', 'FALSE', 'TRUE', 'STRING', 'RETURN', 'WHILE']

tokens = reservadas + [
    'Punto_Y_coma',
    'Dos_puntos',
    'Igual',
    'Igual_igual',
    'Mayor_que',
    'Menor_que',
    'Mayor_o_igual',
    'Menor_o_igual',
    'Numero',
    'Parentesis_apertura',
    'Parentesis_final',
    'Llave_Apertura',
    'Llave_Cierre',
    'Operador',
    'Condicional',
    'Definicion_funcion',
    'CicloF',
    'Suma',
    'Resta',
    'Multiplicacion',
    'Division',
    'Coma',
    'Punto',
    'Guion_Bajo',
    'Comilla',
    'Comilla_simple',
    'Identificador'
]

# Definición de tokens / reglas
t_ignore = ' \t\n'
t_Punto_Y_coma = ';'
t_Dos_puntos = r':'
t_Igual = r'='
t_Igual_igual = r'=='
t_Mayor_que = r'>'
t_Menor_que = r'<'
t_Mayor_o_igual = r'>='
t_Menor_o_igual = r'<='
t_Numero = r'[0-9]'
t_Parentesis_apertura = r'\('
t_Parentesis_final = r'\)'
t_Llave_Apertura = r'\{'   
t_Llave_Cierre = r'\}'  
t_Suma = r'\+'
t_Resta = r'-'
t_Multiplicacion = r'\*'
t_Division = r'/'  
t_Coma = r','
t_Punto = r'\.'
t_Guion_Bajo = r'_'
t_Comilla = r'"'
t_Comilla_simple = r"'"
t_Identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_VAR(t):
    r'\bvar\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_WHILE(t):
    r'\bfor\b'
    return t

def t_DEF(t):
    r'\bdef\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_STRING(t):
    r'(\'[a-zA-Z0-9_]+\'|\"[a-zA-Z0-9_]+\")'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_error(t):
    t.value = "Caracter desconocido: {}".format(t.value[0])
    t.type = 'ERROR_LEXICO'
    t.lexer.skip(1)
    return t

def analisis(texto):
    lexer = lex.lex()
    lexer.input(texto)
    resultados = []
    for tok in lexer:
        resultados.append((tok.type, tok.value, tok.lexpos))
    return resultados
