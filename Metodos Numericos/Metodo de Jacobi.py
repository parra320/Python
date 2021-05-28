#Metodo de Jacobi

from datetime import datetime
import numpy


now= datetime.now()
fecha=(str(now.day)+":"+str(now.month)+":"+str(now.year))
hora=(str(now.hour)+":"+str(now.minute))
print("\n\tMetodo de Jacobi\n\n"+"Fecha: "+fecha+"\tHora: "+hora)

m=int(input('\nValor de m: '))
n=int(input('Valor de n: '))
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector=numpy.zeros((n))
comp=numpy.zeros((m))

for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"]: "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))

def norm(x):
    s=0.0
    n=len(x)
    for i in range (0,n):
        s=s+x[i]*x[i]
    return s

def Jacobi(A,b,x,mi):
    while mi>0:
        for i in range (0, len(A)):
            sigma=0
            for j in range (0, len(A)):
                if (i<j or i>j):
                    sigma=sigma+(A[i][j]*x[j])
                    x[i] = (b[i]-sigma)/A[i][i]
        mi=mi-1
    return x

x=[0.0]*len(vector)
print("\n\tSolución: ")
print(Jacobi(matrix,vector,x,1000))
print("\n")