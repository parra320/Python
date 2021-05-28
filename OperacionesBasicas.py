#Programa que realice las operaciones basicas dados 2 numeros 

print("\n\tIntroduzca 2 valores enteros")
num1 = int(input("Primer valor: "))
num2 = int(input("Segundo valor: "))

suma = num1 + num2
resta1 = num1 - num2
resta2 = num2 - num1
multi = num1*num2
poten1 = num1**num2
poten2 = num1**num2

print("\tLa suma de ", num1, " y ", num2, " es: ", suma)
print("\tLa resta de ", num1, " menos ", num2, " es: ", resta1)
print("\tLa resta de ", num2, " menos ", num1, " es: ", resta2)
print("\tLa multiplicación de ", num1, " y ", num2, " es: ", multi)

if num2==0:
    print("\tLa division de ", num1, " entre ", num2, " es: indefinido")
else:
    divi1 = num1/num2
    print("\tLa division de ", num1, " entre ", num2, " es: ", divi1)
if num1==0:
    print("\tLa division de ", num2, " entre ", num1, " es: indefinido")
else:
    divi2 = num2/num1
    print("\tLa division de ", num2, " entre ", num1, " es: ", divi2)
if num2==0:
    print("\tEl residuo de ", num1, " entre ", num2, " es: indefinido")
else:
    residuo1 = num1%num2
    print("\tEl residuo de ", num1, " entre ", num2, " es: ", residuo1)
if num1==0:
    print("\tEl residuo de ", num2, " entre ", num1, " es: indefinido")
else:    
    residuo2 = num2%num1
    print("\tEl residuo de ", num2, " entre ", num1, " es: ", residuo2)





print("\tLa potencia de ", num1, " elevado a la ", num2, " es: ", poten1)
print("\tLa potencia de ", num2, " elevado a la ", num1, " es: ", poten2)
