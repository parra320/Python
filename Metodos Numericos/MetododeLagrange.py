#Programar Método de Lagrange

import numpy as np #Libreria os
from datetime import datetime

op="1"

while (op!="3"):
    now= datetime.now()
    fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
    hora=(str(now.hour)+":"+str(now.minute))
    print("\n\tMétodo de Interpolación de Lagrange\n\n"+"Fecha: "+fecha+"\tHora: "+hora)
    print("\n 1)Interpolación de Lagrange con Función\n 2)Interpolación de Lagrange con valores dados de X y Y\n 3)Salir")
    op=input("Elige una opcion: ")

    if op=="1":
        def  f(x):
            return eval(fun)
        n=input("Ingrese el numero de valores de X y Y: ")
        print("Escriba la función de la siguiente forma: \n"+
        "2*x**2 o si es trigonometrica: 4*np.cos(x)")
        fun=input("\nFunción: ")
        x=[]
        y=[]
        m=int(n)
        for i in range(0,m):
            x.append(int(input("Elemento de x: ")))
            y.append(float(f(x[i])))
        
        print("Los valores asignados son: \n\t  x\t  y")
        for i in range (0,m):
            print("\t",x[i],"\t",y[i])

        while (op!="3"):
            print("\n¿De que variable desea encontrar el valor? X/Y\n")
            print(" 1) Y\n 2) X\n 3)Salir")
            op=input("Elige una opcion: ")
            if op=="1":
                a=float(input("Ingrese el valor de X: "))
                retval=0
                for i in range(0,m):
                    prod=1
                    for j in range(0,m):
                        if i!=j:
                            prod=prod*(a-x[j])*1.0/(x[i]-x[j])
                    prod=prod*y[i]
                    retval= retval+prod
                print("El valor de y es: ", retval)
                print("\n")
            elif op=="2":
                a=float(input("Ingrese el valor de Y: "))
                retval=0
                for i in range(0,m):
                    prod=1
                    for j in range(0,m):
                        if i!=j:
                            prod=prod*(a-y[j])*1.0/(y[i]-y[j])
                    prod=prod*x[i]
                    retval= retval+prod
                print("El valor de x es: ", retval)
                print("\n")
            elif op=="3":
                print("Elegiste salir")
                input("Presiona enter para continuar..")
            else:
                print("Opcion no valida")
                print("Presiona enter para continuar")

    elif op=="2":
        n=input("Ingrese el numero de valores de X y Y: ")
        m=int(n)
        x=[]
        y=[]
        for i in range(0,m):
            x.append(float(input("Elemento de x: ")))
            y.append(float(input("Elemento de y: ")))
        print("Los valores asignados son: \n\t  x\t  y")
        for i in range (0,m):
            print("\t",x[i],"\t",y[i])

        while (op!="3"):
            print("\n¿De que variable desea encontrar el valor? X/Y\n")
            print(" 1) Y\n 2) X\n 3)Salir")
            op=input("Elige una opcion: ")
            if op=="1":
                a=float(input("Ingrese el valor de X: "))
                retval=0
                for i in range(0,m):
                    prod=1
                    for j in range(0,m):
                        if i!=j:
                            prod=prod*(a-x[j])*1.0/(x[i]-x[j])
                    prod=prod*y[i]
                    retval= retval+prod
                print("El valor de y es: ", retval)
                print("\n")
            elif op=="2":
                a=float(input("Ingrese el valor de Y: "))
                retval=0
                for i in range(0,m):
                    prod=1
                    for j in range(0,m):
                        if i!=j:
                            prod=prod*(a-y[j])*1.0/(y[i]-y[j])
                    prod=prod*x[i]
                    retval= retval+prod
                print("El valor de y es: ", retval)
                print("\n")
            elif op=="3":
                print("Elegiste salir")
                input("Presiona enter para continuar..")
            else:
                print("Opcion no valida")
                print("Presiona enter para continuar")

    elif op=="3":
        print("Elegiste salir")
        input("Presiona enter para continuar..")
        
    else:
        print("Opcion no valida")
        print("Presiona enter para continuar")


