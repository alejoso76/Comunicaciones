import sympy as sym

T = 2
w0 = sym.pi
t, n = sym.symbols('t n')

#ft = 1/2 + 4 * (sym.pi**2)*sym.cos(w0*t) + 0.44444444*(sym.pi**2)*sym.cos(3*w0*t) +  2 * (0.05 *2*(sym.pi)**2)*sym.cos(5*w0*t) +  2*(0.02040816326*(sym.pi)**2)*2*sym.cos(7*w0*t)


def armonico(n):
    a0=(sym.integrate(t+1, (t,-1,0)) + sym.integrate(-t+1,(t,0,1)))/T
    an=2 * (sym.integrate((t+1)*sym.cos(n*w0*t),(t,-1,0))+sym.integrate((-t+1)*sym.cos(n*w0*t),(t,0,1)))/T
    ft=an*sym.cos(n*sym.pi*t)
    return ft

for i in range (0,8):
    ft1=armonico(i)
ft1=ft1+(1/2)

sym.plot(ft1)
