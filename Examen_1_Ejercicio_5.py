import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Tabla=pd.read_csv('DataCovid.csv',usecols=['location','date','total_deaths'])
Indices=Tabla['location']=='Honduras'
TablaH=Tabla[['location','date','total_deaths']][Indices]
Indices=Tabla['location']=='Guatemala'
TablaG=Tabla[['location','date','total_deaths']][Indices]
TablaH=TablaH.set_index('date')
TablaG=TablaG.set_index('date')
Indices1=np.logical_not(np.isnan(TablaH['total_deaths']))
Indices2=np.logical_not(np.isnan(TablaG['total_deaths']))
Indices=(Indices1)&(Indices2)
SerieH=TablaH['total_deaths'][Indices]
SerieG=TablaG['total_deaths'][Indices]
SerieH.index=pd.to_datetime(SerieH.index)
SerieG.index=pd.to_datetime(SerieG.index)
SerieHMes=SerieH.resample('M').mean()
SerieGMes=SerieG.resample('M').mean()
fig,ax=plt.subplots(1)
SerieHMes.plot(ax=ax,kind='line',alpha=0.5)
SerieH.plot(ax=ax,kind='line')
SerieGMes.plot(ax=ax,kind='line',alpha=0.5)
SerieG.plot(ax=ax,kind='line')
plt.title('Número total de muertes en Honduras y Guatemala\n por covid-19')
plt.legend(['Honduras (Mensual)','Honduras','Guatemala (Mensual)','Guatemala'])
plt.xlabel('fechas')
plt.grid(True)
plt.show()
