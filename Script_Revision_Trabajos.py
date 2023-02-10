#Problema Empaquetar una matriz,Trabajo de David Ordoñez

import numpy as np

print(":::::Matriz original:::::\n")
A=np.array([[1,4,5,0,0,0],
[3,5,7,6,0,0],
[0,1,4,1,8,0],
[0,0,3,3,7,4],
[0,0,0,2,8,1],
[0,0,0,0,5,9]])

print(A,"\n")

print(":::::Matriz por bandas:::::")

n=len(A)
fila=np.zeros(n)
columna=np.zeros(n)

for i in range(0,n):
    x=0
    for j in range(0,n): 
        if A[i][j]==0:
            x=x+0
        else:
            x=x+1
    fila[i]=x

q=max(fila);

for i in range(0,n):
    x=0
    for j in range(0,n): 
        if A[j][i]==0:
            x=x+0
        else:
            x=x+1
    columna[i]=x

p=max(columna);

Q=min(columna);


#Proceso para tener la matriz por bandas
Ab=np.zeros((int(p),n))


for j in range(0,n):
    for i in range(0,int(p)):
     if i+j-int(Q)>=0:
        if i+j-int(Q)<n:
            Ab[i][j]=A[i+j-int(Q)][j]
print(Ab)