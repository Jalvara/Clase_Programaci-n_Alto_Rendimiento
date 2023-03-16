import pp
import numpy
import time
import sys
import scipy

#Observaciones:
"""
Las tareas se van asignando a los trabajadores de manera secuencial. 
Sintaxis: f_k=Works.submit(func_k,args_k,depfuns_k,modules_k)
a. func_k: Es una función definida en Python. 
b. args_k: Son los argumentos para la funcionalidad de func_k
c. depfuns_k: Son las subfunciones que se usan dentro de la función
    func_k.
d. modules_k: En lista los modulos que se usan dentro de la función. 
    Los nombres de los modulos deben ser completos. 
e. Todos los parámetros de submit se dan como tuplas con excepción del primero. 
   Cuando se da una tupla de un solo parámetro t, esto se escribe como (t,).
"""
#Obteniendo el tiempo en ejecución:
"""tiempo1=time.time()
x=0
for i in range(1000000):
    x+=i
print(x)    
tiempo2=time.time()
print("El tiempo transcurrido en segundos es: ",tiempo2-tiempo1)"""
#Ejemplo del uso de la función sunmit. 
def MinimimosCuadrados(A,b):
    sol=scipy.optimize.lsq_linear(A,b)
Works=pp.Server()
print("Trabajadores: ",Works.get_ncpus())    
A=numpy.random.randint(1,100,(1000,1000))
b=numpy.random.randint(1,100,1000)
print("--------------Parte sin el uso del modulo pp----------")
#Numero de veces que se resolvera el sistema
n=20
inicio=time.time()
for k in range(n):
    MinimimosCuadrados(A,b)
fin=time.time()
print("Tiempo requerido (segundos): ",fin-inicio)
print("--------------Parte con el uso del modulo pp----------")
inicio=time.time()
f=[Works.submit(MinimimosCuadrados,(A,b),(),("numpy","scipy")) for k in range(n)]
fin=time.time()
print("Tiempo requerido (segundos): ",fin-inicio)