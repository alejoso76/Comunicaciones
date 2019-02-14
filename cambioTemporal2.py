import sympy as sym
sym.init_printing()

t=sym.symbols('t', real=True)

class rect(sym.Function):
    @classmethod
    def eval(cls, arg):
        return sym.Heaviside(arg+1/2) - sym.Heaviside(arg-1/2)

x=rect(t-1/2) + (2/3)*rect(t-3/2) + (1/3)*rect(t-5/2)
sym.plot(x, (t, -1, 5), ylim=[-0.2, 1.2], ylabel=r'$x(t)$')
