#Metodo de Von Mise

import numpy as np
import scipy.optimize as optimize
from datetime import datetime
from sympy import *



now= datetime.now()
fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
hora=(str(now.hour)+":"+str(now.minute))
print("\n\tMetodo de Von Misses\n\n"+"Fecha: "+fecha+"\tHora: "+hora)
x=Symbol('x')
fun=input("\nFunción: ")
xi=int(input("Introduce el parametro inicial de x: "))
xs=int(input("Introduce el parametro final de x: "))
error=float(input("Introduzca el margen de error: "))
derivada=str((diff(fun, x)))
aprox=(xi-xs)/2


def  f(x):
    return eval(fun)

def  f2(x):
    return eval(derivada)

def Metodo(f,x,f2, N=100, emax=error):
    print("\n{:^20}{:^20}{:^20}{:^20}".format("Iteración","Valor de x","f(x)","error"))
    cons=f2(x)
    for k in range(N):
        xold=x
        x=x-f(x)/cons  
        e=abs((x-xold)/x)
        if e<emax:
            break
        print("{:^20}{:^20.6f}{:^20.6f}{:^20.6f}".format(k,float(x),float(f(x)),float(e)))

Metodo(f,aprox,f2)


