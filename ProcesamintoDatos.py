import numpy as np
import matplotlib.pyplot as plt
#Libreria para tratamiento de datos
import pandas as pd
#Un estilo "bonito" para la salida de los graficos
plt.style.use('ggplot')
#Series
datos=np.random.rand(20)
Serie1=pd.Series(datos)
print(Serie1)
print(Serie1.values)
Serie1.index=['Dato_'+str(k) for k in range(1,21,1)]
print(list(Serie1.index))
print("Accediendo al Dato 5: ",Serie1.Dato_5)
print("Accediendo al Dato 6: ",Serie1['Dato_6'])
#Nombrando a una serie de datos:
Serie1.name="Primera Serie"
print("El nombre de la serie es: ",Serie1.name)
Serie2=pd.Series([1,2,3],name="Primeros numero enteros",index=['primero','segundo','tercero'])
print(Serie2)
#Estadistica descriptiva simple
print("-------Estadistica Descriptiva------")
print(Serie1.describe())
print("Calculando el cuantil 13: ",Serie1.quantile(0.13))
#Graficando la informacion de una serie de datos. 
"""fig,axes=plt.subplots(1,4,figsize=(12,3))
Serie1.plot(ax=axes[0],kind='line')
axes[0].set_title("Tipo lineal")
Serie1.plot(ax=axes[1],kind='bar')
axes[1].set_title("Tipo Barra")
Serie1.plot(ax=axes[2],kind='box')
axes[2].set_title("Caja y bigote")
Serie1.plot(ax=axes[3],kind='pie',textprops={'fontsize':8})
axes[3].set_ylabel(" ")
axes[3].set_title("Tipo Circular")
plt.show()"""
#Apartado de Dataframe
Tabla1=pd.DataFrame([['F','Francisco Morazan'],['O','olancho'],['P','Paraiso']])
print(Tabla1)
print("indices de columna: ",list(Tabla1.columns))
print("indices de fila: ",list(Tabla1.index))
Tabla1.columns=['Letra_inicial','Departamento']
Tabla1.index=['Centro','Derecha','Izquierda']
print(Tabla1)
#Segunda forma de generar una tabla de datos
Matriz2=np.random.randint(1,10,size=(5,4))
filas2=[chr(k) for k in np.random.randint(60,90,5)]
columnas2=[chr(k) for k in np.random.randint(60,90,4)]
Tabla2=pd.DataFrame(Matriz2,index=filas2,columns=columnas2)
print(Tabla2)
#Accediento a las etiquetas de fila y columna
print("Imprimiendo la columna de departamento")
print(Tabla1)
print(Tabla1['Departamento'])
print(Tabla1.Departamento)
print(type(Tabla1.loc['Derecha']))
