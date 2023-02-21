import numpy as np
import itertools as it
import sys
#pip install Pillow
from PIL import Image
import matplotlib.pyplot as plt

"""A1=np.zeros([10,10])
A2=np.random.randint(1,10,[10,10])
#print("El tipo de dato de A1: ",type(A1))
#print("El tamaño del objeto de A1: ",sys.getsizeof(A1))
#Multiplicacion de Matrices
A3=np.matmul(A1,A2)
#print(A3)
#Descomposicion en valores singulares
U,D,VT=np.linalg.svd(A2)
D=np.diag(D)
print(U.shape,D.shape,VT.shape)
A4=A2-np.matmul(U,np.matmul(D,VT))
print(np.round(A4))"""
"""Ejemplo de compresion de imagenes con la factorizacion svd"""
#Cargar la imagen
Archivo=Image.open('Foto_Gris.jpg')
Imagen=np.asarray(Archivo)
print("Tipo de archivo: ",type(Archivo))
print("Tipo de Imagen: ",type(Imagen))
U3,D3,V3=np.linalg.svd(Imagen)
D3=np.diag(D3)
print("Dimension de U3: ",U3.shape)
print("Dimension de D3: ",D3.shape)
print("Dimension de V3: ",V3.shape)
#Ajuste del rango de la matriz
k=40
Imagen1=np.matmul(np.matmul(U3[:,0:k],D3[0:k,0:k]),V3[0:k,:])
print("Dimension de Imagen1: ",Imagen1.shape)
fig,axs=plt.subplots(1,2)
axs[0].imshow(Imagen)
axs[1].imshow(Imagen1)
plt.show()







