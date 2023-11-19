import ply.lex as lex

tokens = (
    'NUMBER',
    'ADD',
    'SUB',
    'MULT',
    'DIV',
    'LPAREN',
    'RPAREN',
    'POW',
    'SIN',
    'COS',
    'TAN',
    'EXP',
    'PI',
    'COMMENT',
    'IDENTIFIER',
    'EQUAL',
)


def t_ADD(t):
    r'\+'
    return t


def t_SUB(t):
    r'-'
    return t


def t_MULT(t):
    r'\*'
    return t


def t_DIV(t):
    r'/'
    return t


def t_LPAREN(t):
    r'\('
    return t


def t_RPAREN(t):
    r'\)'
    return t


def t_POW(t):
    r'\^'
    return t


def t_EXP(t):
    r'exp'
    return t


def t_EQUAL(t):
    r'='
    return t


def t_PI(t):
    r'pi'
    return t


def t_NEG(t):
    r'-'
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_IDENTIFIER(t):
    r'[a-zA-Z_а-яА-Я][a-zA-Z0-9_а-яА-Я]*'
    if t.value.lower() == 'sin':
        t.type = 'SIN'
    elif t.value.lower() == 'cos':
        t.type = 'COS'
    elif t.value.lower() == 'tan':
        t.type = 'TAN'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()