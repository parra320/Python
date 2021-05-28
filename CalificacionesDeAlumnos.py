#Programa para almacenar las calificaciones de un grupo de alumnos

opcion="0"
ListaDeAlumnos=[]

while (opcion!="2"):
    
    print("\n\t \tCalificaciones de los Alumnos \n")
    print(" 1)Ingresar nuevo Alumno/Calificacion \n 2)Salir")
    opcion=input("Elige una opcion: ")

    if opcion=="1":
        Nombre=input("Ingrese el nombre del alumno: ")
        Calificacion=input("Ingrese la calificacion del alumno: ")
        registro= Nombre+","+Calificacion+"\n"
        ListaDeAlumnos.append(registro)
        PromedioGeneral=0.0
    elif opcion=="2":
        print("Gracias Totales")
    else:
        print("Opcion no valida")
print(ListaDeAlumnos)

i=0     #Contador
x=0     #variable para la calificacion
Longitud=0
while i<len(ListaDeAlumnos):
    Longitud= int(len(ListaDeAlumnos[i]))
    if ListaDeAlumnos[i][Longitud-3:Longitud-1]=="10":
        x=float(ListaDeAlumnos[i][Longitud-3:Longitud-1])
    else:
        x=float(ListaDeAlumnos[i][Longitud-2:Longitud-1])
    i=i+1
    PromedioGeneral=PromedioGeneral+x
    print(x)
PromedioGeneral=PromedioGeneral/float(len(ListaDeAlumnos))

archivo= open("Calificaciones.xlsx","a")
archivo.writelines(ListaDeAlumnos)       #Escribe mas de una linea
archivo.write("El promedio general de los alumnos es: "+str(PromedioGeneral))     #Escribe una sola cosa o linea
archivo.close()

archivo= open("Calificaciones.xlsx","r")
contenido=archivo.readlines()
archivo.close()
print(contenido)
