import numpy as np
import matplotlib.pyplot as plt
#Libreria para tratamiento de datos
import pandas as pd
import seaborn as sbs
#Un estilo "bonito" para la salida de los graficos
plt.style.use('ggplot')
#Series
"""datos=np.random.rand(20)
Serie1=pd.Series(datos)
print(Serie1)
print(Serie1.values)
Serie1.index=['Dato_'+str(k) for k in range(1,21,1)]
print(list(Serie1.index))
print("Accediendo al Dato 5: ",Serie1.Dato_5)
print("Accediendo al Dato 6: ",Serie1['Dato_6'])"""
#Nombrando a una serie de datos:
"""Serie1.name="Primera Serie"
print("El nombre de la serie es: ",Serie1.name)
Serie2=pd.Series([1,2,3],name="Primeros numero enteros",index=['primero','segundo','tercero'])
print(Serie2)
#Estadistica descriptiva simple
print("-------Estadistica Descriptiva------")
print(Serie1.describe())
print("Calculando el cuantil 13: ",Serie1.quantile(0.13))"""
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
"""Matriz2=np.random.randint(1,10,size=(5,4))
filas2=[chr(k) for k in np.random.randint(60,90,5)]
columnas2=[chr(k) for k in np.random.randint(60,90,4)]
Tabla2=pd.DataFrame(Matriz2,index=filas2,columns=columnas2)
print(Tabla2)"""
#Accediento a las etiquetas de fila y columna
"""print("Imprimiendo la columna de departamento")
print(Tabla1)
print(Tabla1['Departamento'])
print(Tabla1.Departamento)
print(type(Tabla1.loc['Derecha']))"""
#Procesando una base de datos en formato csv
"""Base1=pd.read_csv('DataAccesoElectricidad.csv',delimiter=',',header=4)
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
plt.show()"""
#Tratamiento de series de tiempo
fechas1=pd.date_range("2021-12-1",periods=10)
#print(list(fechas1))
fechas2=pd.date_range("2023-1-1","2023-1-2",freq='H')
#print(list(fechas2))
Serie1=pd.Series(np.random.rand(100),index=pd.date_range("2023-8-1",periods=100))
#print(Serie1.head(10))
#print("Año: ",Serie1.index[0].year)
#print("Mes: ",Serie1.index[0].month)
#print("Segundos: ",Serie1.index[0].second)
#print("Nanosegundos: ",Serie1.index[0].nanosecond)
#print("Tipo de dato de el indice cero: ",type(Serie1.index[0]))
Periodo1=pd.Period('2023-3-1')
#print("Tipo de dato de un periodo: ",type(Periodo1))
#Obtener los datos de la base de datos de temperaturas
Base3=pd.read_csv('Data_Temperatura.csv',delimiter=' ',names=['tiempo','temperatura'],encoding='utf8')
Base3['tiempo']=Base3['tiempo'].apply(lambda x: x.split(',')[1])
Base3.tiempo=pd.to_datetime(Base3.tiempo.values,unit='s')
Base3=Base3.set_index("tiempo")
#print(Base3.head(5))
#fig,ax=plt.subplots(1,1,figsize=(12,5))
#Base3.plot(ax=ax)
#plt.show()
#Ejercicio: Seleccionar solo los datos del mes de julio
Mask_julio=(Base3.index>='2014-7-1')&(Base3.index<'2014-8-1')
Base3_Julio=Base3[Mask_julio]
#print(Base3_Julio.head(20))
#Agrupamiento Simple
Base4=Base3.reset_index()
print(Base4.head(5))
Base4['mes']=Base4['tiempo'].apply(lambda x: x.month)
Base4=Base4.groupby('mes').aggregate(np.mean)
print(Base4)
