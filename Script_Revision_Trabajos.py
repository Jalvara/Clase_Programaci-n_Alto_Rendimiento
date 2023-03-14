import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbs
import datetime
plt.style.use('ggplot')

RGN1 = pd.read_csv("DataRentaGasNatural.csv",index_col=0, skiprows=range(1,4))
print("Imprime indices")
print(RGN1.index)
print("Imprime la primera fila")
print(RGN1.iloc[0])
# obtener los valores de la quinta fila
headers = RGN1.iloc[0]
# establecer los encabezados de las columnas con los valores de la quinta fila
RGN1 = RGN1.set_axis(headers, axis=1, copy=False)

print("Imprime encabezados de columnas")
print(RGN1.columns)

RGN2 = RGN1[['Country Code', 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]]
RGN2 = RGN2.dropna()
print(RGN2.head(5))

RGN2 = RGN2.set_index("Country Code")


RGN2.columns = pd.to_datetime(RGN2.columns)
RGN2.columns = pd.to_numeric(RGN2.columns.astype(int).astype(str))
print("Imprime las columnas nuevas")
print(RGN2.columns)

europeos = ['ALB', 'AUT', 'BLR', 'BEL', 'BIH', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'DEU', 'GRC', 'HUN', 'ISL', 'ITA', 'XKX', 'LVA', 'LTU', 'LUX', 'MKD', 'MLT', 'MDA', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'RUS', 'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'UKR', 'GBR']

eu_data = RGN2.loc[europeos]
fig1=plt.figure()
eu_data.plot()
# Seleccionar la serie de tiempo correspondiente al código de país 'MNE'
plt.title('Rentas de Gas Natural en Europa (2020)')
plt.xlabel('País')
plt.ylabel('Rentas')




# seleccionar la serie de tiempo de Montenegro y graficarla
mne_series = RGN2.loc['MNE', '2010-01-01':'2020-01-01']

# Graficar la serie de tiempo
mne_series_log = np.log(mne_series)
fig2=plt.figure()
mne_series_log.plot()
plt.title('Rentas de Gas Natural en Montenegro (2010-2020)')
plt.xlabel('Año')
plt.ylabel('Rentas de Gas Natural ')
plt.show()