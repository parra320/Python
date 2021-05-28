from sympy import*
import matplotlib.pyplot as plt


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

    print("{:^10}{:^10}{:^10}{:^10}{:^10}".format("x","y","Δy1","Δy2","Δy3"))
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


    """x=7
    y=eval(funcion)
    print("y={:^6.4}".format(y))"""

    print ("\nCalculo de integrales simples con metodo del trapecio:")
    f = sympify(funcion) #convierte el string en una expresion literal f(x)
    a = int(input("Ingrese el valor inicial: "))
    b = int(input("Ingrese el valor final: "))
    m = cantPoints


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


    print("\t\tArea Bajo la curva= "+str(trapecios(f,a,b,m)))  #el primer parametro debe ser la funcion en expresion literal

    plt.plot(points[0], points[1])
    plt.plot(points[0],points[1],'o',linewidth=2,color='g')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    input()
main()




