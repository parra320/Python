#Programa que permita calcular la presencia en las redes 


AbrirArchivo= open("presenciaderedes.csv", "r")
Contenido= AbrirArchivo.readlines()
AbrirArchivo.close()


valor=[]
valor.append(Contenido[3])
print(type(valor))
print("\n\t¿Que operación quiere realizar?: ")
print("1)Calcular diferencia de cierto aspecto comparando 2 meses \n2)Calcular tasa de crecimiento de una red social")
Operacion= input("Elija una opcion: ")

Meses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

if Operacion=="1":
    print("\n\tElija el primer mes para comparar: ")
    print("1)Enero \t2)Febrero \t3)Marzo \n4)Abril \t5)Mayo \t\t6)Junio \n7)Julio \t8)Agosto \t9)Septiembre \n10)Octubre \t11)Noviembre \t12)Diciembre")
    PrimerMes= input("Elija una Opcion: ")
    print("\n\tElija el segundo mes para comparar: ")
    SegundoMes= input("Elija una Opcion: ")

    if (0<int(PrimerMes) and int(PrimerMes)<=12):
        if (0<int(SegundoMes) and int(SegundoMes)<=12):
            print("\n\t¿De que red social desea conocer la información?")
            print("1)Facebook \t2)Twitter \t3)Youtube")
            RedSocial= input("Elija una opcion: ")
            if RedSocial=="1":
                print("\n\t\tContenedores: \n1)Seguidores \t\t\t2)Porcentaje de Crecimiento \n3)Publicaciones \t\t4)Me gusta en publicaciones \n5)Publicaciones compartidas \t6)Comentarios\n")
                Contenedor= input("Elija una opcion: ")
            elif RedSocial=="2":
                print("\n\t\tContenedores: \n1)Seguidores \t\t2)Porcentaje de Crecimiento \n3)Publicaciones \t4)Retuits \n5)Me Gusta \t\t6)Impactos \n7)Videos \t\t8)Visualizaciones \n9)Comentarios \t\t10)Me Gusta\n")
            elif RedSocial=="3":
                print("\n\t\tContenedores: \n1)Videos \t2)Visualizaciones \n3)Comentarios \t4)Me Gusta")
        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida")
elif Operacion=="2":
    print("\n\tElija el primer mes para comparar: ")
    print("1)Enero \t2)Febrero \t3)Marzo \n4)Abril \t5)Mayo \t\t6)Junio \n7)Julio \t8)Agosto \t9)Septiembre \n10)Octubre \t11)Noviembre \t12)Diciembre")
    PrimerMes= input("Elija una Opcion: ")
    print("\n\tElija el segundo mes para comparar: ")
    SegundoMes= input("Elija una Opcion: ")

    if (0<int(PrimerMes) and int(PrimerMes)<=12):
        if (0<int(SegundoMes) and int(SegundoMes)<=12):
            print("\n\t¿De que red social desea conocer la información?")
            print("1)Facebook \t2)Twitter")
            RedSocial= input("Elija una opcion: ")
            if RedSocial=="1":
                MesInicial= Meses[int(PrimerMes)-1]
                MesFinal= Meses[int(SegundoMes)-1]
                ValorDeMesInicial= int(Contenido[1][int(PrimerMes+2)])
                ValorDeMesFinal= int(Contenido[1][int(SegundoMes+2)])
                print(ValorDeMesFinal)
                TasaDeIncremento= float(((ValorDeMesFinal-ValorDeMesInicial)/ValorDeMesInicial)*100)
                print("La Tasa de Incremento entre el mes de",MesInicial,"y el mes de",MesFinal,"es ",TasaDeIncremento)
            elif RedSocial=="2":
                print("cuack2")
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida")
else:
    print("Opcion no valida")

"""print("\n\tElija el primer mes para comparar: ")
print("1)Enero \t2)Febrero \t3)Marzo \n4)Abril \t5)Mayo \t\t6)Junio \n7)Julio \t8)Agosto \t9)Septiembre \n10)Octubre \t11)Noviembre \t12)Diciembre")
PrimerMes= input("Elija una Opcion: ")
print("\n\tElija el segundo mes para comparar: ")
SegundoMes= input("Elija una Opcion: ")

if (0<int(PrimerMes) and int(PrimerMes)<=12):
    if (0<int(SegundoMes) and int(SegundoMes)<=12):
        print("\n\t¿De que red social desea conocer información?")
        print("1)Facebook \t2)Twitter \t3)Youtube")
        RedSocial= input("Elija una opcion: ")
        if RedSocial=="1":
            print("\n\t\tContenedores: \n1)Seguidores \t\t\t2)Porcentaje de Crecimiento \n3)Publicaciones \t\t4)Me gusta en publicaciones \n5)Publicaciones compartidas \t6)Comentarios\n")
            Contenedor= input("Elija una opcion: ")
        elif RedSocial=="2":
            print("\n\t\tContenedores: \n1)Seguidores \t\t2)Porcentaje de Crecimiento \n3)Publicaciones \t4)Retuits \n5)Me Gusta \t\t6)Impactos \n7)Videos \t\t8)Visualizaciones \n9)Comentarios \t\t10)Me Gusta\n")
        elif RedSocial=="3":
            print("\n\t\tContenedores: \n1)Videos \t2)Visualizaciones \n3)Comentarios \t4)Me Gusta")

        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida")
else:
    print("Opcion no valida")"""



