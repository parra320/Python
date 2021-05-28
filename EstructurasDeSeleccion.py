#Programa que determina si un valor entero es positivo o negativo

a= int(input("Ingrese un numero entero: "))

if a>0:
    print(a, " es un entero positivo")
elif a==0:
    print(a, " es un elemento neutro")
elif a<0:
    print(a, " es un elemento negativo")

"""if a>=0:
    print(a, " es un entero positivo o el numero neutro")
else:
    print(a, " es un entero negativo")"""

