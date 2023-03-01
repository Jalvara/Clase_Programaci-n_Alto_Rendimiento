import numpy as np
import sys
import inspect
#Uso de matrices esparcidas
from scipy import sparse as sp
#Construccion de un vector esparcido
vector1=sp.csr_array([1,0,0,3,2,0,0]) 
vector2=np.array([1,2,3,4,5,6,7])
print("Vector Esparcido: \n",vector1)
print("Dimensiones: ",vector1.shape)
x=vector1.dot(vector2)
print("Producto interior entre vector 1 y vector 2: ",x)
print("La salida del producto punto entre el vector 1 y 2 es: ", type(x))
#construccion de matrices esparcidas
#Formato para guardar matrices: CSR, CSC, COO.
Matriz1=np.random.randint(0,3,[10,10])
Smatriz1=sp.csr_matrix(Matriz1)
print("Almacenamiento en memoria de Matriz1: ",sys.getsizeof(Matriz1))
print("Almacenamiento en memoria de Smatriz1: ",sys.getsizeof(Smatriz1))
#Producto matricial Smatriz1*Smatriz1
Matriz2=Smatriz1.multiply(Matriz1)
print("Tipo de la Matriz2: ", type(Matriz2))
#Factorizacion LU de Smatriz1
Obj1=sp.linalg.splu(Smatriz1)
#print(inspect.getmembers(Obj1))
print("Matriz L de la factorizacion LU de Smatriz1: \n",Obj1.L)
print("Formalto de la Matriz L de la factorizacion LU de Smatriz1: \n",type(Obj1.L))
#Ejercicio 1: Elabore un experimento con una matriz de tamaño 10x10
# con entradas en los enteros en el intervalo [0,3].
#Transformar esta matriz al formato CSC 
#Posteriormente investigue como usar la funcion svds para matrices esparciadas
#y finalmente verfique que dicha factorizacion es Correcta. 