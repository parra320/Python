

print("Hola, vamos a generar una contraseña \n")

nombre = input("Ingresa tu primer nombre: ")

print("Hola ", nombre)

print(nombre.upper())

print(nombre.lower())

edad = int(input("¿Cual es tu edad? \n"))

parte1 = nombre[2]

parte2 = str(3*edad/2)

parte3 = nombre[0]

contraseña = parte1+parte2+parte3

print("Tu contraseña asignada es: ", contraseña)
