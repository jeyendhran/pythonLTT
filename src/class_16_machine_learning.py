import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# To work with iris data set
# iris = load_iris()
# print(iris)
# X = iris.data[50:150] # returns the input data second index is for features index
# Y = iris.target[50:150] # returns the output 0 or 1 or 2
# print(X,Y)
# print(np.count_nonzero(Y)) # to get count of non-zeros
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
# print(X_train.size,X_train.shape)
# print(X_test.size)
# ppn = Perceptron(max_iter=20, eta0=0.1,random_state=0) #eta0 is learning rate
# print(ppn)
# ppn.fit(X_train,Y_train)
# print(ppn)
# print(ppn.coef_) # weightages of the features
# Y_train_pred = ppn.predict(X_train)
# Y_pred = ppn.predict(X_test)
# print("Misclassfied in testing",(Y_test - Y_pred).sum()) # returns the deviation of generated algm's o.p with original o.p
# print("Misclassfied in training",(Y_train - Y_train_pred).sum())

# To work with wine data set
# wine = pd.read_csv('wine.csv',header=None)
# Y = wine.iloc[:,0].values
# X = wine.iloc[:,1:].values
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
# print(X_train.size,X_train.shape)
# print(X_test.size)
# ppn = Perceptron(max_iter=50, eta0=0.1) #eta0 is learning rate
# print(ppn)
# ppn.fit(X_train,Y_train)
# print(ppn)
# print(ppn.coef_) # weightages of the features
# Y_train_pred = ppn.predict(X_train)
# Y_pred = ppn.predict(X_test)
# print("Misclassfied in testing",(Y_test - Y_pred).sum())
# print("Misclassfied in training",(Y_train - Y_train_pred).sum())

#Logistic regression on iris data set
# iris = load_iris()
# X = iris.data[50:150] # returns the input data second index is for features index
# Y = iris.target[50:150] # returns the output 0 or 1 or 2
# print(X,Y)
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
# print(X_train.size,X_train.shape)
# print(X_test.size)
# ppn = LogisticRegression(penalty='l1',C=1.0)
# print(ppn)
# ppn.fit(X_train,Y_train)
# print(ppn)
# print(ppn.coef_) # weightages of the features
# Y_train_pred = ppn.predict(X_train)
# Y_pred = ppn.predict(X_test)
# print("Misclassfied in testing",(Y_test - Y_pred).sum()) # returns the deviation of generated algm's o.p with original o.p
# print("Misclassfied in training",(Y_train - Y_train_pred).sum())

# Decision tree
iris = load_iris()
X = iris.data[50:150] # returns the input data second index is for features index
Y = iris.target[50:150] # returns the output 0 or 1 or 2
print(X,Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
print(X_train.size,X_train.shape)
print(X_test.size)
ppn = DecisionTreeClassifier(max_depth=4)
ppn.fit(X_train,Y_train)
print(ppn)
#Y_train_pred = ppn.predict(X_train)
Y_pred = ppn.predict(X_test)
print("Misclassfied in testing",(Y_test - Y_pred).sum()) # returns the deviation of generated algm's o.p with original o.p
#print("Misclassfied in training",(Y_train - Y_train_pred).sum())

df = pd.DataFrame([[1,np.nan,3,np.nan,5,6],[3,4,5,np.nan,7,8],[np.nan,np.nan,np.nan,6,7,8]])

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

imr = Imputer(missing_values='NaN',strategy='mean',axis=1) # axis 0 is column and 1 is for row
imr = imr.fit(df)
print(imr.transform(df.values))

df = pd.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.6,'class3']],columns=['color','size','price','brand'])
df1 = pd.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.6,'class3']],columns=['color','size','price','brand'])
print(df)
size_map = {'XL':3,'L':2,'M':1}
df['size']=df['size'].map(size_map) # to map values with integer values
print(df)
class_map = {l:idx for idx,l in enumerate(np.unique(df['brand']))}
df['brand']=df['brand'].map(class_map)
print(df)
size_map = {v:k for k,v in size_map.items()}
print(size_map)

X = df[['color','size','price']].values
class_le = LabelEncoder()
X[:,0] = class_le.fit_transform(X[:,0])
print(X)

# To change column data to row data
ohe = OneHotEncoder(categorical_features=[1]) 
print(ohe.fit_transform(X).toarray())

# Manually standardize and normalize the data
df = pd.DataFrame([0,1,2,3,4,5])
df[1] = (df[0]-df[0].mean())/df[0].std(ddof=0) # to get standarsized data
df[2] = (df[0]-df[0].min())/(df[0].max()-df[0].min()) # to get normalized data
df.columns = ['input','standardized','normalized']
print(df)


# To standardize the training and test data to get exact result in all passes
iris = pd.read_csv("wine.csv")
X = iris.iloc[:,1:].values
Y = iris.iloc[:,0].values
# X = iris.data[50:150] # returns the input data second index is for features index
# Y = iris.target[50:150] # returns the output 0 or 1 or 2
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train) # to standardize the training data
X_test_std = sc.fit_transform(X_test)   # to standardize the testing data
ppn = Perceptron(max_iter=50, eta0=0.1) #eta0 is learning rate
ppn.fit(X_train_std,Y_train)
Y_pred = ppn.predict(X_test_std)
print("Misclassfied in testing",(Y_test - Y_pred).sum()) # returns the deviation of generated algm's o.p with original o.p


