#Programa que determina valores par e impares de una lista


#ListaDeNumerosEnteros=[2,8,20,12,4,7,9,13,1,5]

"""pedro=[2.3]
Lista=[2,3,pedro]


print(Lista)"""


#Registro de calificaciones

print("\t\t\t Programa que realiza el registro de las calificaciones del curso Python \n")

opcion="0"
datos=[]

#diferente !=

while (opcion!="2"):
    print("1)llenar \n2)salir \n")
    opcion=input("Elige una opción: ")
    if opcion=="1":
        nombre=input("Ingresa el nombre del alumno: ")
        cal=input("Ingresa la califación del alumno: ")
        registro= nombre+","+ cal+"\n"
        datos.append(registro)
    elif opcion=="2":
        print("Gracias totales")
    else:
        print("Opción no válida jaja")

print(datos)

archivo= open("calificaciones.csv","a")
#archivo.write() #Una sola cosa o linea
archivo.writelines(datos) #Escribe en mi archivo más de una linea
archivo.close()

a=open("calificaciones.csv","r")
contenido=a.readlines()
a.close()

print(contenido)