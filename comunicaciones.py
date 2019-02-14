
import sympy as sym

a, b, c, t=sym.symbols('a b c t')

xt=a*sym.sin(t) + b*sym.sin(2*t)
'''
def idSenSuma(x, y):
    return sym.sin(x)*sym.cos(y) + sym.sin(y)*sym.cos(x)

print idSenSuma(30, 60)
'''
sym.plot(xt)
