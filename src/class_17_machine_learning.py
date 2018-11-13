import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine.csv',header=None)
wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash',  'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
	            'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
Y = wine.iloc[:,0].values
X = wine.iloc[:,1:].values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

lr = LogisticRegression(penalty='l1',C=0.1) # l1 is linear and l2 is quadtratic
lr.fit(X_train,Y_train)
print("Training Accuracy",lr.score(X_train,Y_train))
print("Testing Accuracy",lr.score(X_test,Y_test))   # will predict and calculate the accuracy in percentage
print(lr.coef_) # weightage to the features

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
weight,params = [],[]
for i in np.arange(-4.,6.):
    lr = LogisticRegression(penalty='l1', C=10.**i, random_state=0)
    lr.fit(X_train_std,Y_train)
    weight.append(lr.coef_[1])
    params.append(10.**i)

print(weight)

colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'pink', 'lightgreen', 'lightblue',  'gray', 'indigo', 'orange']

weight_array = np.array(weight)

for column,color in zip(range(weight_array.shape[1]),colors):
    plt.plot(params,weight_array[:,column],
             label=wine.columns[column+1],
             color=color)


plt.xlim([10**-5,10**5])
plt.xscale('log')
plt.legend(loc='best')
ax = plt.axes()
ax.legend(loc='upper left')
plt.show()