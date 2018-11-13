from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pydotplus
from sklearn import tree
import matplotlib.pyplot as plt
from IPython.display import Image,display

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

clf = tree.DecisionTreeClassifier()
clf = ppn.fit(iris.data,iris.target)

dot_Data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True)
grph = pydotplus.graph_from_dot_data(dot_Data)
display(Image(data=grph.create_png()))
