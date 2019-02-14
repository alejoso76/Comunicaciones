
import sympy as sym
t=sym.symbols('t')

xt=4*sym.sin(7*t) + 25*sym.cos(15*t)
sym.plot(xt, xlim=[-1, 7])
