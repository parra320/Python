#Metodo de Biseccíon

from math import *
from pickle import LONG
from pylab import *
from MetodoDeBiseccion import*

def f(x):
    return eval(fun)

#definición de la función
fun=input("funcion: ")
#leer parametros
xi=float(input("Ingrese el parametro inicial de x: "))
xs=float(input("Ingrese el parametro final de x: "))
error=float(input("Ingrese el intervalo de error: "))

raiz=biseccion(f,xi,xs,error)
if isinstance(raiz(int,long,float,complex)):
    print ("La raiz es ",raiz)

    #crear la grafica
    x=arange(xi,xs,error*10)
    y=eval(fun)
    plot(x,y,'b-',raiz,f(raiz),'rio')
    title(fun)
    xlabel('x')
    ylabel('y')
    text(raiz,f(raiz), 'Raiz')
    grid(True)
    show()
    print (raiz)
else:
    print(raiz)