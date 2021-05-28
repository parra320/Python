#Programa para calcular el area de un circulo
import math

print("\n\t\tEste Programa detremina el Area de un Circulo\n")
Radio=float(input("Ingrese el valor del Radio: "))

def AreaDelCirculo(Radio):
    return Radio**2*math.pi

AreaDelCirculo(Radio)

print("El Area de un Circulo de Radio: ",Radio,
" es igual a: ",AreaDelCirculo(Radio))



"""print(math.pi)
print(math.sin(math.pi/4))
print(math.cos(math.pi/2))
print(math.sqrt(4))
print(math.exp(3))"""