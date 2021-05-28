from datetime import datetime
from sympy import*
import matplotlib.pyplot as plt

op="1"

while (op!="3"):
    now= datetime.now()
    fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
    hora=(str(now.hour)+":"+str(now.minute))
    print("\n\tMétodo de Integración Trapezoidal\n\n"+"Fecha: "+fecha+"\tHora: "+hora)
    print("\n 1)Area Bajo la Curva\n 2)Metodo de Integración Trapezoidal\n 3)Salir")
    op=input("Elige una opcion: ")

    if op=="1":
        print ("\n\tREGLA COMPUESTA DEL TRAPECIO\n\n")
        def main():
            grado=1
            cantPoints = int(input("Ingrese cantidad de puntos conocidos > "))\
        
            if cantPoints < 2:
                print ("\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n")
                main()\
        
            points = [[],[],[],[],[]]
        
            for i in range(cantPoints):
                print ("\n( x",i,",y",i,")")
                x = int(input("Ingrese 'x' > "))
                y = int(input("Ingrese 'y' > "))
                points[0].append(x)
                points[1].append(y)        
            points[2].append(" ")
            points[3].append(" ")
            points[3].append(" ")
            points[4].append(" ")
            points[4].append(" ") 
            points[4].append(" ")
            for i in range(cantPoints-1):
                del1=int(points[1][i+1])-int(points[1][i])
                points[2].append(del1)
            for i in range(cantPoints-2):
                del2=int(points[2][i+2])-int(points[2][i+1])
                points[3].append(del2)
            for i in range(cantPoints-3):
                del3=int(points[3][i+3])-int(points[3][i+2])
                points[4].append(del3)
            
            h=float(points[0][1]-points[0][0])
            Vdel1=float(points[2][1]/h)
            Vdel2=float(points[3][2]/(2*h**2))
            Vdel3=float(points[4][3]/(6*h**3))
            y0=float(points[1][0])
            x0=float(points[0][0])
            if(Vdel1>0):
                if(x0>0):                
                    funcion= (str(y0)+"+"+str(Vdel1)+"*x-"+str(Vdel1*x0))
                else:
                    funcion= (str(y0)+"+"+str(Vdel1)+"*x+"+str(Vdel1*-x0))
            else:
                if(x0>0):
                    funcion= (str(y0)+str(Vdel1)+"*x+"+str(-Vdel1*x0))
                else:                
                    funcion= (str(y0)+str(Vdel1)+"*x-"+str(Vdel1*x0))

            print("\n{:^10}{:^10}{:^10}{:^10}{:^10}".format("x","y","Δy1","Δy2","Δy3"))
            for i in range (0,cantPoints):            
                print("{:^10}{:^10}{:^10}{:^10}{:^10}".format(points[0][i],points[1][i],points[2][i],points[3][i],points[4][i]))

            if (points[3][cantPoints-1]==points[3][cantPoints-2] and points[3][cantPoints-1]==points[3][cantPoints-3] and points[3][cantPoints-1]!=" "):
                grado=2

            if (points[4][cantPoints-1]==points[4][cantPoints-2] and points[4][cantPoints-1]==points[4][cantPoints-3] and points[4][cantPoints-1]!=" "):
                grado=3    
                
            if(grado>=2):
                if(Vdel2>0):
                    if(x0>0):                
                        funcion=funcion+"+"+str(Vdel2)+"*x**2-"+str(2*x0*Vdel2)+"*x+"+str(Vdel2*x0**2)+"-"+str(h*Vdel2)+"*x+"+str(h*x0*Vdel2)
                    else:
                        funcion=funcion+"+"+str(Vdel2)+"*x**2+"+str(-2*x0*Vdel2)+"*x+"+str(Vdel2*x0**2)+"-"+str(h*Vdel2)+"*x"+str(h*x0*Vdel2)
                else:
                    if(x0>0):     
                        funcion=funcion+str(Vdel2)+"*x**2+"+str(-2*x0*Vdel2)+"*x"+str(Vdel2*x0**2)+"+"+str(-h*Vdel2)+"*x"+str(h*x0*Vdel2)
                    else:
                        funcion=funcion+str(Vdel2)+"*x**2-"+str(2*x0*Vdel2)+"*x"+str(Vdel2*x0**2)+"+"+str(-h*Vdel2)+"*x+"+str(h*x0*Vdel2)
                    

            if(grado>=3):
                if(Vdel3>0):
                    if(x0>0):                
                        funcion=funcion+"+"+str(Vdel3)+"*x**3-"+str(3*x0*Vdel3)+"*x**2+"+str(Vdel3*x0**2*3)+"*x-"+str(Vdel3*x0**3)+"-"+str(Vdel3*3*h)+"*x**2+"+str(Vdel3*6*x0*h)+"*x-"+str(Vdel3*3*x0**2*h)+"+"+str(Vdel3*2*h**2)+"*x-"+str(Vdel3*2*x0*h**2)
                    else:
                        funcion=funcion+"+"+str(Vdel3)+"*x**3+"+str(-3*x0*Vdel3)+"*x**2+"+str(Vdel3*x0**2*3)+"*x+"+str(-Vdel3*x0**3)+"-"+str(Vdel3*3*h)+"*x**2"+str(Vdel3*6*x0*h)+"*x-"+str(Vdel3*3*x0**2*h)+"+"+str(Vdel3*2*h**2)+"*x+"+str(Vdel3*-2*x0*h**2) 
                else:
                    if(x0>0):     
                        funcion=funcion+str(Vdel3)+"*x**3+"+str(-3*x0*Vdel3)+"*x**2"+str(Vdel3*x0**2*3)+"*x+"+str(-Vdel3*x0**3)+"+"+str(-Vdel3*3*h)+"*x**2"+str(Vdel3*6*x0*h)+"*x+"+str(Vdel3*-3*x0**2*h)+str(Vdel3*2*h**2)+"*x+"+str(Vdel3*-2*x0*h**2)
                    else:
                        funcion=funcion+str(Vdel3)+"*x**3-"+str(3*x0*Vdel3)+"*x**2"+str(Vdel3*x0**2*3)+"*x+"+str(-Vdel3*x0**3)+"+"+str(-Vdel3*3*h)+"*x**2+"+str(Vdel3*-6*x0*h)+"*x+"+str(Vdel3*-3*x0**2*h)+str(Vdel3*2*h**2)+"*x"+str(Vdel3*-2*x0*h**2)

            print("\n\tLa función obtenida es de grado", grado)

            print ("\nCalculo de integrales simples con metodo del trapecio:")
            f = sympify(funcion) #convierte el string en una expresion literal f(x)
            a = int(input("Ingrese el valor inicial: "))
            b = int(input("Ingrese el valor final: "))
            m = cantPoints
            areatotal=0
            for i in range(cantPoints-1):
                valx=points[0][i]
                valx2=points[0][i+1]
                valy=points[1][i]
                valy2=points[1][i+1]
                base=valx2-valx
                area=base*((valy+valy2)/2)
                areatotal=areatotal+area

            def trapecios(f,a,b,m):
                h = (b-a)/float(m)
                s = 0
                n = 0
                a_evaluado = 0
                b_evaluado = 0

                for i in range(1,m):
                    n = a + (i*h)
                    n_evaluado = f.evalf(subs = {"x" : n}) #evalua n en la funcion descrita
                    s = s + n_evaluado

                a_evaluado = f.evalf(subs = {"x" : a}) #evalua a en la funcion descrita, lo mismo con b en la siguiente linea
                b_evaluado = f.evalf(subs = {"x" : b})
                resul = h/2 * (a_evaluado + 2*s + b_evaluado)

                return resul
            resultado=trapecios(f, a, b, m)
            print("\tArea Bajo la curva resultante: ",resultado,"\n\t\tAreaTotal Verdadera: ", areatotal)  #el primer parametro debe ser la funcion en expresion literal

            errorporcent=abs((areatotal-resultado)/areatotal)*100
            print("\t\tPorcentaje de Error: ", errorporcent)
            

            plt.plot(points[0], points[1])
            plt.plot(points[0],points[1],'o',linewidth=2,color='g')
            plt.fill_between(points[0], points[1])
            plt.grid()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()

            input()
        main()


    elif op=="2":
        cantPoints = int(input("Ingrese cantidad de puntos conocidos > "))\
 
        if cantPoints < 2:
            print ("\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n")
    
        points = [[],[],[]]
    
        for i in range(cantPoints):
            print ("\n( x",i,",y",i,")")
            x = float(input("Ingrese 'x' > "))
            y = float(input("Ingrese 'y' > "))
            z = float(x*y)
            points[0].append(x)
            points[1].append(y)
            points[2].append(z)
    
        print("\nLos valores asignados son: \n\t Tiempo\t  Velocidad  Desplazamiento")
        print("\t",points[0][0],"\t  ",points[1][0],"\t    ",points[2][0])
        for i in range (1,cantPoints):
            print("\t",points[0][i],"\t  ",points[1][i],"  ",points[2][i])
        while (op!="3"):
            print("\n¿A partir de que variable desea conocer los demas valores? \n1)Tiempo \n2)Velocidad \n3)Desplazamiento \n4)Salir \n")
            op=input("Elige una opcion: ")
            if op=="1":
                a=float(input("Ingrese el valor de Tiempo: "))
                retval=0
                retval2=0
                for i in range(0,cantPoints):
                    prod=1
                    prod2=1
                    for j in range(0,cantPoints):
                        if i!=j:
                            prod=prod*(a-points[0][j])*1.0/(points[0][i]-points[0][j])
                            prod2=prod2*(a-points[0][j])*1.0/(points[0][i]-points[0][j])
                    prod=prod*points[1][i]
                    prod2=prod2*points[2][i]
                    retval= retval+prod
                    retval2=retval2+prod2
                print("El cohete lleva una Velocidad de:",retval,"millas/segundo, recorriendo :", retval2, "millas")
                print("\n")
            elif op=="2":
                a=float(input("Ingrese el valor de Velocidad: "))
                retval=0
                retval2=0
                for i in range(0,cantPoints):
                    prod=1
                    prod2=1
                    for j in range(0,cantPoints):
                        if i!=j:
                            prod=prod*(a-points[1][j])*1.0/(points[1][i]-points[1][j])
                            prod2=prod2*(a-points[1][j])*1.0/(points[1][i]-points[1][j])
                    prod=prod*points[0][i]
                    prod2=prod2*points[2][i]
                    retval= retval+prod
                    retval2=retval2+prod2
                print("El cohete logra esa velocidad en:",retval,"segundos, recorriendo :", retval2, "millas")
                print("\n")
            elif op=="3":
                a=float(input("Ingrese el valor de desplazamiento: "))
                retval=0
                retval2=0
                for i in range(0,cantPoints):
                    prod=1
                    prod2=1
                    for j in range(0,cantPoints):
                        if i!=j:
                            prod=prod*(a-points[2][j])*1.0/(points[2][i]-points[2][j])
                            prod2=prod2*(a-points[2][j])*1.0/(points[2][i]-points[2][j])
                    prod=prod*points[1][i]
                    prod2=prod2*points[0][i]
                    retval= retval+prod
                    retval2=retval2+prod2
                print("El cohete lleva una Velocidad de:",retval,"millas/segundo, en :", retval2, "segundos")
                print("\n")
            elif op=="4":
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









