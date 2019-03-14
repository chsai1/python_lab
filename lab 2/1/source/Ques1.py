from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
data_set =pd.read_csv('train.csv') #to read the data from train.csv file
data_set['Embarked'] = data_set['Embarked'].map({'Q': 1, 'S': 0 ,'C':2}) # replacing the alphabetical values
data_set['Sex'] = data_set['Sex'].map({'female': 1, 'male': 0}) # assigning values like 1 for female and 0 for male

data_set.select_dtypes(include=[np.number]).interpolate().dropna() #replacing all the null values
print("Data Analysis using Naïve Baye’s, SVM and KNN Classifiers")
print(data_set[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean()) #mean of the survived for 2 different sex columns
print(" ")

print(data_set[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean())  #printing the mean of the survived Pclass values
data_set['Age'].fillna(data_set['Age'].mean(),inplace =True)
data_set = data_set.dropna(how='any',axis=0)
print(" ")
print(data_set[['Embarked', 'Survived']].groupby(['Embarked'], as_index=False).mean()) #mean of the survived for different embarked values after converting to numerical

data_set=data_set.drop(columns=['Name','SibSp','Parch','Ticket','Fare','Cabin']) #eliminating the unused attributes from csv file
train,test=train_test_split(data_set,test_size=0.2)
train_label=train['Survived']
train=train.drop(columns=['Survived'])
test_label=test['Survived']
test=test.drop(columns=['Survived'])

NBClassifier=GaussianNB()  #Fitting the data to Naive Bayes Classifier
NBClassifier.fit(train,train_label)

SVMClassifier=SVC()  #Fitting the data for Support Vector Classifier
SVMClassifier.fit(train,train_label)

KNNClassifier=KNeighborsClassifier(n_neighbors=2)   #Fitting the data to K-Nearest Neighbour classifier code
KNNClassifier.fit(train,train_label)

naive_bayes_result= NBClassifier.score(test,test_label)
svm_result=SVMClassifier.score(test,test_label)
knn_result=KNNClassifier.score(test,test_label)
print(" ")
print("Score for Naive Bayes is: ")
print("-------------------------")
print(naive_bayes_result)
print(" ")
print("Score for Support Vector Classifier is: ")
print("-------------------------")

print(svm_result)
print(" ")
print("Score for KNN Classifier is : ")
print("-------------------------")
print(knn_result)