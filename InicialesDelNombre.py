#Programa que pida el nombre completo y regrese las iniciales dle usuario

print("\n\tInroduzca su nombre empezando por Mayusculas conforme se le vaya solicitando")
nom1 = input("Primer Nombre: ")
nom2 = input("(En caso de no tener segundo nombre agregue un *)\nSegundo Nombre: ")
ape1 = input("Apellido Paterno: ")
ape2 = input("Apellido Materno: ")

if nom2== "*":
    iniciales = nom1[0]+"."+ape1[0]+"."+ape2[0]+"."
else:
    iniciales = nom1[0]+"."+nom2[0]+"."+ape1[0]+"."+ape2[0]+"."



print("\tSus iniciales son: ", iniciales)