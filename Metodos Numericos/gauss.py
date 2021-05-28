

def mostrarmatriz (matriz, orden):
    for i in range(0, orden):
        linea = "| "
        for j in range(orden+1):
            linea += str(matriz [i][j]) + ""
        linea += "| "
        print(linea)

matriz = [[8.53, 6.72, 3.99, 8.47, -11.69] , [12.84, -17.52, 2.72, 10.71, 6.99] , [6.28, 2.27, -8.62, -4.98, 18.32]]

#Orden de la matriz
orden = len(matriz)
mostrarmatriz(matriz, orden)

#Recorrer la matriz
for j in range(0, orden + 1):
    for i in range(0, orden):
        if i > j:
            #Dividir los elementos de la matriz
            division = matriz[i][j] / matriz[j][j]
            for k in range(0, orden + 1):
                #Obtener el nuevo valor para los elelmentos de la diagonal
                matriz[i][k] = matriz[i][k] - division*matriz[j][k]
#Recorrer matriz
x = [0, 0, 0]
for i in range(orden, 0, -1):
    suma = 0
    for j in range(i, orden):
        suma = suma + matriz[i-1][j]*x[j]
    #Obtener los valores de las variables
    x[i-1] = ((matriz[i-1][orden]-suma)/matriz[i-1][i-1])

#Mostrar los valores de las variables
for i in range(0, orden):
    print("x" + str(i)+ " = " + str(x[i]))