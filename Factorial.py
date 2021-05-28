#Programa que determina el factorial de un numero

n=int(input("Ingrese un numero entero: "))

i=n-1
factorial=n
while i>0:
    factorial=factorial*i
    i=i-1
print(factorial)
