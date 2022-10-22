import os
import sys
import ply.lex as lex


class TokenError(Exception):
    pass


reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "out": "OUT"
}

tokens = [
    'ID',
    'EQ',
    'EPS',
    'ASSIGN',
    'SEMICOLON',
    'NUM',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'POW',
    'LBR',
    'RBR',
    *reserved.values()
]

t_SEMICOLON = r'\;'
t_ASSIGN = r'\='
t_EQ = r'\=\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_POW = r'\*\*'
t_LBR = r'\('
t_RBR = r'\)'

t_ignore = ' \t'

<<<<<<< Updated upstream:error-production/lex.py
def t_newline(t):
  r'\n+'
  t.LEXER.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.LEXER.skip(1)
  
=======

def t_ID(t: ply.lex.LexToken):
    r"""[A-Za-z][A-Za-z0-9_]*"""
    t.type = reserved.get(t.value, "ID")
    return t


def t_NUM(t: ply.lex.LexToken):
    r"""[0-9]+"""
    t.value = int(t.value)
    return t


def t_newline(t: ply.lex.LexToken):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t: ply.lex.LexToken):
    raise TokenError(f"Syntax error: Illegal character '{t.value[0]}'.")

>>>>>>> Stashed changes:src/lex.py

lexer = lex.lex()


def main():
    if len(sys.argv) == 1:
        exit("Waiting your file ...")

    if not os.path.exists(sys.argv[1]):
        exit("File not found ...")

    file_path = os.path.abspath(sys.argv[1])

    with open(file_path, "r", encoding="utf-8") as read_lang, open(
            file_path + ".out", "w"
    ) as write_lang:
        for line in read_lang.readlines():
            lexer.input(line.rstrip())

            while True:
                try:
                    token = lexer.token()
                except TokenError as e:
                    exit(*e.args)

                if not token:
                    break

                print(token, file=write_lang)

    print("File is processed ...")


if __name__ == "__main__":
    main()
