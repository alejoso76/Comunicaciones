#Determinar periodo

import sympy as sym

sym.init_printing()
t, sigma, omega, T=sym.symbols('t sigma omega T', real=True)

funo=4*sym.sin(7*t) + 25*sym.cos(15*t)
fdos=(6*sym.sin(3*t) + 4*sym.sin(7*t))**2

print funo
print fdos
#sym.plot(sym.re(funo))
#sym.plot(sym.re(fdos))
sym.plot(sym.sin(t))
