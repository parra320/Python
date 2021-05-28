#Programa para calcular el area de un rectangulo

print("\n\t\tEste Programa detremina el Area de un Rectangulo\n")
Base=float(input("Ingrese el valor de la Base: "))
Altura=float(input("Ingrese el valor de la Altura: "))

def AreaDelRectangulo(Base, Altura):
    return Base*Altura

AreaDelRectangulo(Base,Altura)

print("El area de un rectangulo de base: ",Base,
" y Altura: ",Altura," es: ",AreaDelRectangulo(Base,Altura))


#AreaDelRectangulo(15,10)             #Metodo Estatico

"""print("El area de un rectangulo de base: ",Base,
" y Altura: ",Altura," es: ",AreaDelRectangulo(15,10))"""

