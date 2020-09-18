from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

def calculateFormula(formula, params):
    expr = parse_expr(formula)
    _, _, _ = symbols('A B C')
    return expr.evalf(9, subs=params)