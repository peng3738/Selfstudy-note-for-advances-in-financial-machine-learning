from sympy import *
init_printing(use_unicode=False,wrap_line=False,no_global=True)
p,u,d=symbols('p u d')
m2=p*u**2+(1-p)*d**2
m1=p*u+(1-p)*d
v=m2-m1**2
factor(v)
