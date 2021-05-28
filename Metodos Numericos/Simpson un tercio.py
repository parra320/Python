from sympy import*
import matplotlib.pyplot as plt
from datetime import datetime

now= datetime.now()
fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
hora=(str(now.hour)+":"+str(now.minute))
print("\n\tMétodo de Simpson 1/3\n\n"+"Fecha: "+fecha+"\tHora: "+hora)
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


    print("La función obtenida es de grado", grado)

    """x=7
    y=eval(funcion)
    print("y={:^6.4}".format(y))"""

    f = sympify(funcion) #convierte el string en una expresion literal f(x)

    def simpson13(f, a, b):
        m=(a+b)/2
        a_evaluado = f.evalf(subs = {"x" : a}) #evalua a en la funcion descrita
        b_evaluado = f.evalf(subs = {"x" : b})
        m_evaluado = f.evalf(subs = {"x" : m})
        integral= -(a-b)/6*(a_evaluado+(4*m_evaluado)+b_evaluado)
        return integral

    areatotal=0

    for i in range(cantPoints-1):
        valx=points[0][i]
        valx2=points[0][i+1]
        valy=points[1][i]
        valy2=points[1][i+1]
        base=valx2-valx
        area=base*((valy+valy2)/2)
        areatotal=areatotal+area
    
    a = int(input("Ingrese el valor inicial: "))
    b = int(input("Ingrese el valor final: "))
    n=2
    h=(b-a)/n
    suma=0
    for i in range(n):
        b=a+h
        area=simpson13(f, a, b)
        suma= suma+area
        a=b
    print("\tArea Bajo la curva resultante: ",suma,"\n\t\tAreaTotal Verdadera: ", areatotal)
    errorporcent=abs((areatotal-suma)/areatotal)*100
    print("\tPorcentaje de Error: ", errorporcent)

    plt.plot(points[0], points[1])
    plt.plot(points[0],points[1],'o',linewidth=2,color='g')
    plt.fill_between(points[0], points[1])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    input()
main()

