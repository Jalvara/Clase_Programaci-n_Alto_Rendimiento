import numpy as np
#Uso de matrices esparcidas
from scipy import sparse as sp
#Construccion de un vector esparcido
vector1=sp.csr_array([1,0,0,3,2,0,0]) 
vector2=np.array([1,2,3,4,5,6,7])
print("Vector Esparcido: \n",vector1)
print("Dimensiones: ",vector1.shape)
x=np.dot(vector1,vector2)
print("Producto interior entre vector 1 y vector 2: ",x)

