import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline

df = pd.read_csv("wdbc.csv",header=None)
X = df.loc[:,2:].values
Y = df.loc[:,1].values
l = LabelEncoder()
y = l.fit_transform(Y)
print(y) # M is 1 and B is 0
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)

pipe = Pipeline([('sc',StandardScaler()),
                 ('pca',PCA(n_components=5)),
                 ('lr',LogisticRegression(penalty='l1'))
                ])

pipe.fit(X_train,Y_train)
Y_pred = pipe.predict(X_test)
print("Test accuracy",pipe.score(X_test,Y_test))
print("Misclassfied",(Y_test-Y_pred).sum())
print(confusion_matrix(Y_test,Y_pred))