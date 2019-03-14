from sklearn.cross_validation import train_test_split
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt



dataset = pd.read_csv('forestfires.csv')

#null values checking
dataset.isnull().sum().sort_values(ascending=False)

#table for missing values
missing= dataset.isnull().sum().sort_values(ascending=False)
percent= (dataset.isnull().sum()/dataset.isnull().count())
total= pd.concat([missing, percent],axis=1, keys=["Total", "Percent"])
print(total)

#get categorial values
categorical= dataset.select_dtypes(include=[np.object])
categorical.sample(5)

#changing non numeric into numeric
dataset["month"].value_counts()



y = dataset['temp']

X = dataset.drop(['month'],axis=1)
X = pd.get_dummies(X, columns=["day"])





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
model = lm.fit(X_train,y_train)

predictions = lm.predict(X_test)
print(predictions)



print ('RMSE is: \n', mean_squared_error(y_test, predictions))
print ("R^2 is: \n", model.score(X_test, y_test))
