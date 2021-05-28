#Programa que suma los primeros cien numeros

"""n = int(input("dime el numero hasta el que deseas sumar"))

suma = n*(n+1)/2

print("La suma de los numeros hasta el ", n," es ", suma)"""

"""m=int(input("\nDime el numero en el que deseas comenzar la suma: "))
n=int(input("Dime el numero hasta el que deseas sumar: "))
j=int(input("Dime el intervalo en el que deseas sumar: "))

a=0"""

"""for i in range (1, n+1, 1):
    a=a+i
    #print(a)
    1~ i=1, a=0+1=1
    2~ i=2, a=1+2=3
    3~ i=3, a=3+3=6
    4~ i=4, a=6+4=10
    5~ i=5, a=10+5=15
print(a)"""


"""for i in range (m, n+1, 1):
    a=a+i 
print("La suma de numeros desde ",m," hasta ", n," es: ")"""


"""for i in range (m, n+1, j):
    a=a+i
print("La suma de numeros desde ",m," hasta ", n," en intervalos de ", j, " es: ")"""

#Metodo de Gauss usando el ciclo while 

a=0 
i=1 
while(a<101):
    a=a+i
    i=i+1
    """ 1~ viejo valor: a=0, i=1 ~ nuevo valor: a=0+1=1, i=1+1=2
    2~ viejo valor: a=1, i=2 ~ nuevo valor: a=1+2=3, i=2+1=3
    3~ viejo valor: a=3, i=3 ~ nuevo valor: a=3+3=6, i=3+1=4"""
print("La suma de los primeros cien numeros es: ", a)
