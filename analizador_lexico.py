import ply.lex as lex

reservadas_path = "P_reservadas.txt"
tokens_path = "tokens.txt"

with open(reservadas_path, "r") as reservadas_file:
    reservada = [line.strip() for line in reservadas_file if line.strip()]

with open(tokens_path, "r") as tokens_file:
    tokens = reservada + [line.strip() for line in tokens_file if line.strip()]

t_Punto_Y_coma = ';'
t_Dos_puntos = r':'
t_Igual = r'='
t_Igual_igual = r'=='
t_Mayor_que = r'>'
t_Menor_que = r'<'
t_Mayor_o_igual = r'>='
t_Menor_o_igual = r'<='
t_Numero = r'[a-z]*[a-z]'
t_Contenido = r'C'
t_Parentesis_apertura = r'\('
t_Parentesis_final = r'\)'

lexema = []

def t_Declaracion_variable(t):
    r'\bvar\b'
    return t

def t_Condicional(t):
    r'\bif\b'
    return t

def t_Definicion_funcion(t):
    r'\bdef\b'
    return t

def t_CicloF(t):
    r'\bfor\b'
    return t

def t_IN(t):
    r'in\b'
    return t

def t_Espacios(t):
    r'\s+'
    pass

def t_Variable(t):
    r'[a-z]*[a-z]'
    return t

def t_Valor(t):
    r'(-?\d+\.\d+)|(-?\d+)|("[^"]+")'
    return t

def analisis(data):
    global lexema

    analizador = lex.lex()
    analizador.input(data)

    lexema.clear()
    while True:
        token = analizador.token()
        if not token:
            break
        estado = "{:16} {:16} {:4}".format(str(token.type), str(token.value), str(token.lexpos))
        lexema.append(estado)
    return lexema

def t_error(t):
    global lexema
    estado = "ERROR {:16} {:4}".format(str(t.value), str(t.lexpos))
    lexema.append(estado)
    t.lexer.skip(1)
