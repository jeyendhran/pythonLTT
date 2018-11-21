import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

wine = pd.read_csv('wine.csv',header=None)
wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash',  'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
	            'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
Y = wine.iloc[:,0].values
X = wine.iloc[:,1:].values

iris = load_iris()
X = iris.data[:]
Y = iris.target[:]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

# to standardize the data sets
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

from sklearn.decomposition import PCA

pca = PCA(2)
print(X_train_std)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca = pca.fit_transform(X_test_std)
print(X_train_pca)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train_pca,Y_train)
print("Test accuracy",lr.score(X_test_pca,Y_test))
print("Training accuracy",lr.score(X_train_pca,Y_train))

