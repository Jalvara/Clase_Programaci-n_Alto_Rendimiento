import tensorflow as tf
from sklearn import metrics
from tensorflow.keras.layers import Dense
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
import numpy as np
import keras
import matplotlib.pyplot as plt
import pickle
#Presentacion de la base de datos de Keras
#Python Deep Learning, Jordi Torres.
mnist=tf.keras.datasets.mnist
print(type(mnist))
(x_train,y_train),(x_test,y_test)=mnist.load_data()
print(x_train.ndim)
print(x_train.shape)
print(y_train[15])
#Graficando los datos
"""fig=plt.figure()
for k in range(16):
    fig.add_subplot(4,4,k+1)
    plt.imshow(x_train[k],cmap=plt.cm.binary)
plt.show()"""
#Normalizacion
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255
#Vectorizacion
x_train=x_train.reshape(60000,784)
x_test=x_test.reshape(10000,784)
#Categorizando las salidas
y_train=to_categorical(y_train,num_classes=10)
y_test=to_categorical(y_test,num_classes=10)
print(y_train[15])
"""model=keras.Sequential()
model.add(Dense(10,activation='sigmoid',input_shape=(784,)))
model.add(Dense(10,activation='softmax'))
model.compile(loss="categorical_crossentropy",optimizer='sgd',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5)
FileObj=open('Data1.obj','wb')
pickle.dump(model,FileObj)
FileObj.close()"""
"""FileObj=open('Data1.obj','rb')
model=pickle.load(FileObj)
FileObj.close()
test_loss,test_acc=model.evaluate(x_test,y_test)
print('Precision de la prueba: ',test_acc)
y_pred=model.predict(x_test)
def f(y):
    n,m=y.shape
    salida=[]
    for k in range(n):
        salida.append(np.argmax(y[k]))
    return np.array(salida)
print(metrics.confusion_matrix(f(y_test),f(y_pred)))"""