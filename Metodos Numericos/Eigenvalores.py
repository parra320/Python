import numpy as np 


m=int(input('\nValor de m: '))
n=int(input('Valor de n: '))
matrix = np.zeros((m,n))

print ('Método de Eigenvalores')
print ('Introduce la matriz de coeficientes\n')

for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento A["+str(r+1)+str(c+1)+"]: "))
print("A: \n", matrix)

eigenvalue,eigenvector = np.linalg.eig(matrix)

print("\nPrimer tupla: ", eigenvalue)
#print("Segunda tupla: \n", eigenvector)