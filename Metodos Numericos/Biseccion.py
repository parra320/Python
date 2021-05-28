#Programa para determinar el metodo de bisección

from tkinter import *
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

def  f(x):
    return eval(fun)


def biseccion(f, xi, xs, error):
    xm=(xi+xs)/2.0
    i=0
    print("{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","xi","xs","xm","error"))
    while abs(f(xm))>error:
        i=i+1
        xm=(xi+xs)/2.0
        if f(xi)*f(xm) <0:
            xs=xm
        else:
            xi=xm
        print("{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}".format(i,float(xi),float(xs),float(xm),float(f(xm))))
    print("La raiz es: ",xm)
    return xm

def funcion(xi, xs):
    func1=""
    func2=""
    if(xi>f(xi)):
        func1="creciente"
    if(xi<f(xi)):
        func1="decreciente"
    if(xs>f(xs)):
        func2="decreciente"
    if(xs<f(xs)):
        func2="creciente"
    print("La función es "+func1+" desde "+str(xi)+" hasta la raiz y "+func2+" desde la raiz hasta "+str(xs))

now= datetime.now()
fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
hora=(str(now.hour)+":"+str(now.minute))
print("\nMetodo de Bisección\n"+"Fecha: "+fecha+"\tHora: "+hora)
print("Ingrese la función de la siguiente manera: \n"
+"2*x**3+11*x**2+7*x-3")

fun=input("\nFunción: ")
xi=int(input("Introduce el parametro inicial de x: "))
xs=int(input("Introduce el parametro final de x: "))
error= float(input("Introduce el indice de error: "))
print("\n")
xm=(xi+xs)/2.0
i=0
raiz=biseccion(f, xi, xs, error)
valor=funcion(xi, xs)

x=np.arange(xi*2, xs*2, 0.2)
y=eval(fun)
plt.title("Metodo de Bisección")
plt.plot(x, y/3000, 'b-')
plt.grid(True)
plt.show()