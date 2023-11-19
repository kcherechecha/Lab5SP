import ply.yacc as yacc
import math
from lex import tokens

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('nonassoc', 'NEG'),
    ('left', 'POW'),
)

variables = {}


def p_statement(p):
    '''statement : assignment
                 | expression'''
    p[0] = p[1]


def p_assignment(p):
    'assignment : IDENTIFIER EQUAL expression'
    variables[p[1]] = p[3]
    p[0] = p[3]


def p_add(p):
    'expression : expression ADD expression'
    p[0] = p[1] + p[3]


def p_sub(p):
    'expression : expression SUB expression'
    p[0] = p[1] - p[3]


def p_mult(p):
    'expression : expression MULT expression'
    p[0] = p[1] * p[3]


def p_div(p):
    'expression : expression DIV expression'
    p[0] = p[1] / p[3]


def p_neg(p):
    "expression : SUB expression %prec NEG"
    p[0] = -p[2]


def p_pow(p):
    'expression : expression POW expression'
    p[0] = p[1] ** p[3]


def p_exp(p):
    'expression : EXP'
    p[0] = math.exp(p[1])

def p_pi(p):
    'expression : PI'
    p[0] = math.pi

def p_comment(p):
    'expression : COMMENT'

def p_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_sin(p):
    'expression : SIN LPAREN expression RPAREN'
    p[0] = math.sin(p[3])


def p_cos(p):
    'expression : COS LPAREN expression RPAREN'
    p[0] = math.cos(p[3])


def p_tan(p):
    'expression : TAN LPAREN expression RPAREN'
    p[0] = math.tan(p[3])


def p_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_error(p):
    print("Syntax error")


def p_expression_var(p):
    'expression : IDENTIFIER'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined name '{p[1]}'")
        p[0] = 0

parser = yacc.yacc()