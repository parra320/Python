#Programa que compara 2 numeros para saber quien es mayor o si son iguales

print("\n\t\tEste programa compara 2 numeros enteros")
print("\tSi el primer numero es mayor al segundo se devolvera el valor 1\n"+
"\tSi el segundo numero es mayor al primero se devolvera el valor -1\n"+
"\tSi ambos numeros son iguales se devolvera el valor 0\n")
PrimerNumero=int(input("Ingrese el Primer numero a comparar: "))
SegundoNumero=int(input("Ingrese el Segundo numero a comparar: "))
valor=20

def Comparacion(PrimerNumero, SegundoNumero):
    if PrimerNumero>SegundoNumero:
        return 1
    elif PrimerNumero<SegundoNumero:
        return -1
    elif PrimerNumero==SegundoNumero:
        return 0
    else: 
        print("No se cumplen los parametros para comparar")

print("El valor es igual a: ", Comparacion(PrimerNumero,SegundoNumero))

