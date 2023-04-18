import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import patsy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def plot_y_contour(ax, Y, title,fig,X1,X2):
    c = ax.contourf(X1, X2, Y, 15, cmap=plt.cm.RdBu)
    ax.set_xlabel(r"$x_1$", fontsize=20)
    ax.set_ylabel(r"$x_2$", fontsize=20)
    ax.set_title(title)
    cb = fig.colorbar(c, ax=ax)
    cb.set_label(r"$y$", fontsize=20)
"""y=np.array([1,2,3,4,5])
x1=np.array([6,7,8,9,10])
x2=np.array([11,12,13,14,15])
data={"y":y,"x1":x1,"x2":x2}
y,X=patsy.dmatrices("y~x1*x2-1",data)
y,Z=patsy.dmatrices("y~x1:x2",data)
print("------------------Diferencias entre * y :------------------------")
print("Salida con * ")
print(X)
print("Salida con : ")
print(Z)
print("-----------------Uso de data Frame-------------------------------")
data_df=pd.DataFrame(data)
y,W=patsy.dmatrices("y~x1*x2",data_df,return_type="dataframe")
print(W)
print("-----------------Metodos de resolucion---------------------------")
print("(A) Usando el modulo de numpy.linalg: ")
Sol=np.linalg.lstsq(np.array(W),np.array(y))
print(Sol[0])
print("(B) Usando el modulo de statsmodels.api: ")
Sol1=sm.OLS(y,X)
print(Sol1.fit().params)
print("(C) Usando el modulo de statsmodels.formula.api: ")
Sol2=smf.ols("y~x1*x2",data)
print(Sol2.fit().params)"""
#Ejemplo aplicado de un modelo de regresión lineal
N=100
x1=np.random.randn(N)
x2=np.random.randn(N)
data=pd.DataFrame({"x1":x1,"x2":x2})
def y_true(x1,x2):
    return 1+2*x1+3*x2+4*x1*x2
data["y_true"]=y_true(x1,x2)
e=0.5*np.random.randn(N)
data["y"]=data["y_true"]+e
model=smf.ols("y~x1*x2-1",data)
result=model.fit()
def GraficoQQ(result):
    fig,ax=plt.subplots(figsize=(8,4))
    smg.qqplot(result.resid,ax=ax)
    plt.show()
#GraficoQQ(result)
def Script1(result):
    x = np.linspace(-1, 1, 50)
    X1, X2 = np.meshgrid(x, x)
    new_data = pd.DataFrame({"x1": X1.ravel(), "x2": X2.ravel()})
    y_pred = result.predict(new_data)
    y_pred.shape
    y_pred = y_pred.values.reshape(50, 50)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    plot_y_contour(axes[0],y_true(X1,X2),"Relacion Verdadero",fig,X1,X2)
    plot_y_contour(axes[1],y_pred,"Ajuste de modelo",fig,X1,X2)
    plt.show()
Script1(result) 