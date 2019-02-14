import sympy as sym
T=2; W0=sym.pi
t, n=sym.symbols('t n')

print 'ao='
a0=(sym.integrate(t+1, (t, -1, 0)) + sym.integrate(-t+1, (t, 0, 1)))/T
sym.pprint(a0)

print 'an='
an=2*(sym.integrate((t+1)*sym.cos(n*W0*t), (t, -1, 0)) + sym.integrate((-t+1)*sym.cos(n*W0*t), (t, 0, 1)))/T
sym.pprint(an)

print 'bn='
bn=2*(sym.integrate((t+1)*sym.sin(n*W0*t), (t, -1, 0)) + sym.integrate((-t+1)*sym.sin(n*W0*t), (t, 0, 1)))/T
sym.pprint(bn)
