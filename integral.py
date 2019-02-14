import sympy as sym
from sympy import *
T = 2
w0 = sym.pi
t, n = sym.symbols('t n')
'''a0 = (sym.integrate(t+1, (t,-1,0)) + sym.integrate(-t+1,(t,0,1)))/T
sym.pprint(a0)
an = 2 * (sym.integrate((t+1)*sym.cos(n*w0*t),(t,-1,0))+sym.integrate((-t+1)*sym.cos(n*w0*t),(t,0,1)))/T
sym.pprint(an)
bn = 2 * (sym.integrate((t+1)*sym.sin(n*w0*t),(t,-1,0))+sym.integrate((-t+1)*sym.sin(n*w0*t),(t,0,1)))/T
sym.pprint(bn)
'''
ft = 1/2 + 4 * (sym.pi**2)*sym.cos(w0*t) + 0.44444444*(sym.pi**2)*sym.cos(3*w0*t) +  2 * (0.05 *2*(sym.pi)**2)*sym.cos(5*w0*t) +  2*(0.02040816326*(sym.pi)**2)*2*sym.cos(7*w0*t)


sym.plot(ft)
