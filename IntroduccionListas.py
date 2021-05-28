#Instrucciones con Listas

a=[1,3,-3,2]

print(a,"\n")

"""for i in a:
    print(i)"""

#Agrega un valor al final de la Lista
a.append(2)
print(a,"\n")

#Agrega un valor (Posicion en la Lista, Valor a agregar)
a.insert(2,6)
print(a,"\n")

#Remueve el primer valor que sea igual a el valor brindado
a.remove(2)
print(a,"\n")

#Crea una nueva lista a base de la anterior pero ordenando los valores de menor a mayor
b=sorted(a)
print(b)
print(a,"\n")

#Ordena la Lista actual de menor a mayor
a.sort()
print(a,"\n")

#Longitud de la cadena
print("La longitud de la cadena es igual a: ",len(a),"\n")

#Lugar que ocupa un valor especifico en una lista
print("El lugar que ocupa -3 en la Lista es: ", a.index(-3))

#Valores maximos y minimos de una Lista
print("El valor maximo de la lista es: ", max(a))
print("El valor minimo de la lista es: ", min(a))

