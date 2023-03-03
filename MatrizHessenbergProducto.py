import numpy as np

def Producto(A,v):
    r=len(v)
    (n,m)=np.shape(A)
    B=A-v[0]*np.eye(n)
    C=np.zeros([n,n])
    for a in range(1,r,1):
        print(a)
        C=np.matmul(B,A-v[a]*np.eye(n))
        B=C.copy()
    return B[:,0]    
def Producto1(A,v):
    r=len(v)
    B=np.zeros([r+1,r])
    C=np.zeros([r+1,r])
    B=A[0:r+1,0:r].copy()
    for s in range(r):
        B[s][s]-=v[0]
    print("Matriz B:\n ",B)
    print("Matriz A: ",A)
    for a in range(1,r):
        for j in range(0,r-a,1):
            for i in range(r+1):
                print("(",i,",",j,")")
                C[i][j]=0
                for k in range(max(0,i-a-1),j+2,1):
                    print("(i,k,j): ",i,k,j,":",B[i][k],A[k][j])
                    C[i][j]=C[i][j]+B[i][k]*A[k][j]
                    if k==j:
                        print("a: ",v[a])
                        C[i][j]=C[i][j]-v[a]*B[i][k]
        print("--->",C)
        B=C.copy()
    return B[:,0]            
A=np.array([[2,3,4,5],[1,2,3,6],[0,7,6,5],[0,0,23,1]])
I=np.eye(4)
print(np.matmul(A-I,A-2*I))
l=np.array([1,2])
B=Producto(A,l)
print(B)
