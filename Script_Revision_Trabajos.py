#Prueba1 Ejercicio 4 Escribir la funcion B=f(A,v) donde v es vector de k elementos 
#A una matriz cuadrada y B=(A-v(0)I)...(A-v(k-1)I)
import numpy as np
def f(Ai,v):
    import numpy as np
    k=len(v)
    n=len(Ai)
    print(n)
    A=Ai.copy()   

    for i in range(0,n):
        A[i][i]=Ai[i][i]-v[0]
    
    B=A.copy()
   
    for r in range(1,k):
        for i in range(0,n):
            A[i][i]=Ai[i][i]-v[r]

        C=np.zeros([n,n])
        

        for i in range(0,n):
            for j in range(0,n):
                C[i][j]=C[i][j]+np.dot(B[i][:],A[:][j])
        B=C
    print('La primera columna es \n', B[:][1])   
    return B[:][1]  
#Ai=np.array([[2,3,4,-5], [1,0,3,0], [2,4,6,3], [5,3,0,-5]])
#v=[4,5,1,-1,5]
Ai=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(Ai)
v=np.array([1,2,3])
f(Ai,v)