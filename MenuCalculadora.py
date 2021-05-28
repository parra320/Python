#Programar una calculadora

import os #Libreria os

op="1"

while (op!="6"):
    
    os.system("cls")  #Limpiar mi terminal
    print("\n\t \tBienvenidos a mi calculadora \n")
    print(" 1)Suma\n 2)resta\n 3)Multiplicacion\n"+ 
    " 4)Division\n 5)Conversion\n 6)Salir")
    op=input("Elige una opcion: ")

    if op=="1":
        print("Elegiste Suma")
        dig1=float(input("Ingresa el Primer valor: "))
        dig2=float(input("Ingresa el Segundo valor: "))
        ope= dig1+dig2
        print("La suma de ",dig1, " mas ", dig2, " es igual a: ", ope)
        input("Presiona enter para continuar..")
        os.system("cls")

    elif op=="2":
        print("Elegiste Resta")
        dig1=float(input("Ingresa el Primer valor: "))
        dig2=float(input("Ingresa el Segundo valor: "))
        ope= dig1-dig2
        print("La Resta de ",dig1, " menos ", dig2, " es igual a: ", ope)
        input("Presiona enter para continuar..")
        os.system("cls")

    elif op=="3":
        print("Elegiste Multiplicacion")
        dig1=float(input("Ingresa el Primer valor: "))
        dig2=float(input("Ingresa el Segundo valor: "))
        ope= dig1*dig2
        print("La Multiplicacion de ",dig1, " y ", dig2, " es igual a: ", ope)
        input("Presiona enter para continuar..")
        os.system("cls")

    elif op=="4":
        print("Elegiste Division")
        dig1=float(input("Ingresa el Primer valor: "))
        dig2=float(input("Ingresa el Segundo valor: "))
        ope= dig1/dig2
        print("La Division de ",dig1, " entre ", dig2, " es igual a: ", ope)
        input("Presiona enter para continuar..")
        os.system("cls")

    elif op=="5":
        print("Elegiste Conversion")
        input("Presiona enter para continuar..")
        op2="1"
        while op2!=3:
            print("\n\t\t Sistema de Conversiones \n")
            print("1)Binario a decimal \n2)Octal a decimal \n3)Salir")
            op2=input("Elige una opcion: ")

            if op2=="1":
                print("Elegiste conversion binaria a decimal")
                Numero=int(input("Ingrese un numero: "))
                def Factorial(Numero):
                    if Numero==0:
                        return 1
                    elif Numero<0:
                        print("Ingrese un valor entero positivo")
                    else: 
                        return Numero*Factorial(Numero-1)
                print("El factorial de: ",str(Numero)," es: ",str(Factorial(Numero)))
                print("Presiona enter para continuar")

            elif op2=="2":
                print("Elegiste conversion Octal a decimal")
                print("Presiona enter para continuar")

            elif op2=="3":
                print("Elegiste Salir")
                print("Presiona enter para continuar")

            else:
                print("Opcion no valida")
                print("Presiona enter para continuar")

    elif op=="6":
        print("Elegiste salir")
        input("Presiona enter para continuar..")
        
    else:
        print("Opcion no valida")
        print("Presiona enter para continuar")


