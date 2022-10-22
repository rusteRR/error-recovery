import sys
from typing import List

import ply.yacc as yacc
from printer import Printer
from lex import tokens

ERROR_MSG = {
    ";": "Found unexpected semicolon before else"
}

VARIABLES = {}


precedence = (
  ('left', 'PLUS', 'MINUS'),
  ('left', 'MULT', 'DIV'),
  ('right', 'POW')
)


class Condition:
    def __init__(self, bool_expr: str, statement: str, else_statement: str):
        self.bool_expr = bool_expr
        self.statement = statement
        self.else_statement = else_statement
        self.exit_code = 0


class Error:
    def __init__(self):
        self.exit_code = 1


def p_if_statement(p):
    """
    if_statement : IF bool_expr THEN statement else_part
    """
    if any([token is None for token in [p[1], p[2], p[3], p[4], p[5]]]):
        p[0] = Error()
        return
    p[0] = Condition(p[2], p[4], p[5])


def p_start(p):
    """
    bool_expr : ID EQ ID
    """

    p[0] = " ".join([p[1], p[2], p[3]])


def p_statement_to_id(p):
    """
    statement: ID ASSIGN ID SEMICOLON
    """

    VARIABLES[p[1]] = VARIABLES.get(p[3], 0)


def p_statement_to_expr(p):
    """
    statement: ID ASSIGN expr SEMICOLON
    """

    VARIABLES[p[1]] = p[3]


def p_output(p):
    """
    out: OUT expr
       | OUT statement
    """

    OUTFILE.write(f"{p[1]}\n")


def p_statement(p):
    """
    statement: statement
    """

    p[0] = p[1]


def p_else_part(p):
    """
    else_part :      ELSE statement SEMICOLON
                   | empty
                   | SEMICOLON ELSE statement SEMICOLON
    """

    if len(p) == 5:
        PRINTER.print_error(OUTFILE, ERROR_MSG[p[1]], [p[1], p[2], p[3], p[4]], 0)
        return
    if len(p) == 2:
        return

    p[0] = p[2]


def p_expr_plus(p):
    """expr : expr PLUS expr"""
    p[0] = p[1] + p[3]


def p_expr_minus(p):
    """expr : expr MINUS expr"""
    p[0] = p[1] - p[3]


def p_expr_mult(p):
    """expr : expr MULT expr"""
    p[0] = p[1] * p[3]


def p_expr_div(p):
    """expr : expr DIV expr"""
    p[0] = p[1] / p[3]


def p_expr_pow(p):
    """expr : expr POW expr"""
    p[0] = p[1] ** p[3]


def p_expr_num(p):
    """expr : NUM"""
    p[0] = p[1]


def p_expr_br(p):
    """expr : LBR expr RBR"""
    p[0] = p[2]


# def p_empty(p):
#     """empty :"""
#     pass


def p_error(p):
    print("Error")


PRINTER = Printer()
PARSER = yacc.yacc()
OUTFILE = ""


def main():
    if len(sys.argv) == 1:
        exit("Args error: Waiting your file ...")

    if not os.path.exists(sys.argv[1]):
        exit("Args error: File not found ...")

    file_path = os.path.abspath(sys.argv[1])

    with open(file_path, "r", encoding="utf-8") as code_in, open(
            f"{file_path}.out", "w"
    ) as code_out:

        OUTFILE = code_out

        for line in code_in.readlines():
            try:
                PARSER.parse(line)
            except (ParserError, TokenError) as e:
                exit(*e.args)

        # output

    print("File is processed ...")

<<<<<<< Updated upstream:error-production/parse.py
    text = file.read()
    result = parser.parse(text)
    if result.exit_code == 1:
        return
    printer.print_condition(result, outfile)
=======
>>>>>>> Stashed changes:src/parse.py


if __name__ == "__main__":
    main()
