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
"""Tabla1=pd.DataFrame([['F','Francisco Morazan'],['O','olancho'],['P','Paraiso']])
print(Tabla1)
print("indices de columna: ",list(Tabla1.columns))
print("indices de fila: ",list(Tabla1.index))
Tabla1.columns=['Letra_inicial','Departamento']
Tabla1.index=['Centro','Derecha','Izquierda']
print(Tabla1)"""
#Segunda forma de generar una tabla de datos
Matriz2=np.random.randint(1,10,size=(5,4))
filas2=[chr(k) for k in np.random.randint(60,90,5)]
columnas2=[chr(k) for k in np.random.randint(60,90,4)]
Tabla2=pd.DataFrame(Matriz2,index=filas2,columns=columnas2)
print(Tabla2)
#Accediento a las etiquetas de fila y columna
"""print("Imprimiendo la columna de departamento")
print(Tabla1)
print(Tabla1['Departamento'])
print(Tabla1.Departamento)
print(type(Tabla1.loc['Derecha']))"""
#Procesando una base de datos en formato csv
Base1=pd.read_csv('DataAccesoElectricidad.csv',delimiter=',',header=4)
print("Base de dato de acceso a la electricidad: ")
print(Base1)
print("Resumen de la Base de Datos: ")
print(Base1.info())
print("Imprimiendo los primeros 5 encabezados de la Base de datos: ")
print(Base1.head(5))
print(Base1.tail(5))
#Ejercicio1: Crear una columna con igual a la columna '2020' pero con los elementos
#de esta cadena como tipo string.
Base1['2020str']=Base1['2020'].apply(lambda x: str(x))
print(Base1.info())
print(Base1.head(5))
#Ejercicio2: Modificar la columna del nombre de indicador y cambiar las entradas
#eliminando los espacios en blanco y sustituirlos por guiones bajos. 
Base1['Indicator Name']=Base1['Indicator Name'].apply(lambda x: '_'.join(x.split(' '))) 
print(Base1['Indicator Name'])
#Imprimiendo los indices de la base de datos.
print(list(Base1.index))
Base2=Base1.set_index('Country Code').sort_index(level=0)
print("Los indices de la base de de datos Base2: ")
print(list(Base2.index))
#Graficar la informacion del año 2020 para todos los paises. 
Serie3=Base1['2020']
Serie3.index=Base1.set_index('Country Code').index
print("Serie de datos de 2020: ")
print(Serie3)
print("Acceso a la electricidad en Honduras en el anio 2020Ñ ",Serie3['HND'])
Serie4=Serie3.sort_values()
fig,ax=plt.subplots(1)
Serie4.plot(ax=ax,kind='line',style='.-',markevery=5)
ax.set_title('Acceso a la electricidad en el mundo, año 2020')
plt.show()


