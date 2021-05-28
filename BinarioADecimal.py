#Programa para determinar la conversion de un numero binario a decimal

n=int(input("Ingrese el numero binario a convertir: "))

binario=n
i=0
decimal=0
Numbinario=True
while(n>0):
    if n%10>1:
        Numbinario=False
    decimal = decimal+(n%10*2**i)
    n=int(n/10)
    i=i+1
if Numbinario:
    print("El numero binario es ",binario," convertido a decimal es igual a: ", decimal)
else:
    print("No se ingreso un numero binario valido")


"""n1=int(n[0])
n2=int(n[1])
n3=int(n[2])
n4=int(n[3])
m1= n1*(2**3)
m2= n2*(2**2)
m3= n3*(2**1)
m4= n4*(2**0)
res=m1+m2+m3+m4
print("La conversion del numero binario ", n, " es ", res)"""




