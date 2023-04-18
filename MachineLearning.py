import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import patsy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import datasets
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics
from sklearn import tree
from sklearn import neighbors
from sklearn import svm
from sklearn import ensemble
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#Regresion Discreta

"""df=sm.datasets.get_rdataset("iris").data
#print(df)
df_subset = df[df.Species.isin(["versicolor", "virginica"])].copy()
#print(df_subset)
df_subset.Species = df_subset.Species.map({"versicolor": 1,"virginica": 0})
#print(df_subset)
df_subset.rename(columns={"Sepal.Length": "Sepal_Length","Sepal.Width": "Sepal_Width","Petal.Length": "Petal_Length","Petal.Width": "Petal_Width"},inplace=True)
#print(df_subset.head(5))
model = smf.logit("Species ~ Petal_Length + Petal_Width", data=df_subset)
result = model.fit()
print(result.summary())"""
iris = datasets.load_iris()
print(iris.target_names)
print(iris.feature_names)
X_train, X_test, y_train, y_test=model_selection.train_test_split(iris.data, iris.target,train_size=0.7)
classifier = linear_model.LogisticRegression()
classifier.fit(X_train, y_train)
y_test_pred = classifier.predict(X_test)
print(metrics.confusion_matrix(y_test, y_test_pred))
classifier = tree.DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_test_pred = classifier.predict(X_test)
print(metrics.confusion_matrix(y_test, y_test_pred))
