#Programa que solicita un usuario y una contraseña y los almacena

opcion="0"
Datos=[]

while opcion!="2":

    print("\n\t\tIngresar Datos\n")
    print("1)Ingresar nuevo Usuario y Contraseña \n2)Salir")
    opcion=input("Elige una opcion: ")

    if opcion=="1":
        Usuario=input("Ingrese un nombre de Usuario: ")
        Contraseña=input("Ingrese la Contraseña de minimo 8 digitos: ")
        if len(Contraseña)>7:
            registro= Usuario+","+Contraseña+"\n"
            Datos.append(registro)
        else:
            print("La Contraseña es Incorrecta, debe contener minimo 8 digitos")
    elif opcion=="2":
        print("Eligio Salir")
    else: 
        print("Opcion no valida")

archivo= open("Usuarios y Contraseñas.csv", "a")
archivo.writelines(Datos)
archivo.close()

archivo= open("Usuarios y Contraseñas.csv", "r")
informacion= archivo.readlines()
archivo.close()
print(type(informacion))