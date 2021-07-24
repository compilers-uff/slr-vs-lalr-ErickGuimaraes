import ply.yacc as yacc
import ply.lex as lex
import os

if os.path.exists("parser.out"):
  os.remove("parser.out")
  print("Arquivo de saída já existe, removendo arquivo")

if os.path.exists("parsetab.py"):
  os.remove("parsetab.py")
  print("parsetable já existe, removendo arquivo")

inpt = input("Qual valor deseja analisar: ")

if(inpt == ""):
    print("Dando vazio com entrada");
else:
    print("Recebido o valor " + inpt + " para analise");

analyser = input("Qual tipo de Analise deseja Realisar ? (1) LALR , (2) SLR ")

if analyser == "1" or analyser.lower() == "lalr".lower():
    analyser = "LALR"
    print("Usando LALR")

elif analyser == "2" or analyser.lower() == "slr".lower():
    analyser = "SLR"
    print("Usando SLR")

else:
    print("Comando não reconhecido, usando LALR como padrão")
    analyser = "LALR"

# Tokens utilizados no programa

tokens = (
    'NAME', 'NUMBER', 'TIMES','EQUALS',
    )

t_TIMES   = r'\*'
t_EQUALS  = r'='
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Caracteres que serão ignorados (espaço)

t_ignore = " \t"

# Caracter de nova linha

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Erro ao dectar caracteres

def t_error(t):
    print(f"Carcter Ilegal {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()

# Gramática utilizada
#S -> L = R | R
#L -> * R | id
#R -> L

def p_S(p):
    '''S : L EQUALS R
                    | R'''
def p_L(p):
    '''L : TIMES R
                    | TERM'''

def p_R(p):
    '''R : L '''


def p_TERM(p):
    '''TERM : NAME
                | NUMBER '''

def p_error(p):
    print("Erro de sintaxe!")

parser = yacc.yacc(method=analyser)

resultado = parser.parse(inpt)
