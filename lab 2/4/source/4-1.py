from sklearn.cross_validation import train_test_split
from sklearn import datasets
from sklearn.linear_model import LinearRegression

import pandas as pd
from sklearn.metrics import mean_squared_error




dataset = pd.read_csv('forestfires.csv')
dataset.describe()
y = dataset['temp']

X = dataset.drop(['month','day'],axis=1)



X_train, X_test, y_train, y_test = train_test_split(X, y,)

lm = LinearRegression()
model = lm.fit(X_train,y_train)

predictions = lm.predict(X_test)
print(predictions)



print ('RMSE is: \n', mean_squared_error(y_test, predictions))
print ("R^2 is: \n", model.score(X_test, y_test))

