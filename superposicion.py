import sympy as sym
sym.init_printing()
t=sym.symbols('t', real=True)
A=0.3
W1=3
B=0.5
W2=5

x=A*sym.cos(W1*t) + B*sym.cos(W2*t)

sym.plot(x, (t, -5, 5), ylim=[-1.2, 1.2], ylabel=r'$x(t)$')
