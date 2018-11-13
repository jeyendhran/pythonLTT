import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

banking_data = pd.read_csv('banking.csv',header=0)
print(banking_data.head())
print(banking_data['education'].unique())

# To convert the values of 'basic.4y or 6y or 9y' to 'Basic'
banking_data['education'] = np.where(banking_data['education'] == 'basic.9y','Basic',banking_data['education']) # np.where(condition,if true,if false)
banking_data['education'] = np.where(banking_data['education'] == 'basic.6y','Basic',banking_data['education'])
banking_data['education'] = np.where(banking_data['education'] == 'basic.4y','Basic',banking_data['education'])

print(banking_data['education'].unique())

print(banking_data.groupby('y').mean())
print(banking_data.groupby('marital').mean())
print(banking_data.groupby('education').mean())

cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(banking_data[var], prefix=var)
    data1=banking_data.join(cat_list)
    banking_data=data1

cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
data_vars = banking_data.columns.values.tolist()
print(data_vars)
numeric_col = [i for i in data_vars if i not in cat_vars]
print(numeric_col)

data_final = banking_data[numeric_col]

from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

X = data_final.loc[:, data_final.columns != 'y']
y = data_final.loc[:, data_final.columns == 'y']
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

columns = X_train.columns
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
os_data_X,os_data_y=os.fit_sample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])

# we can Check the numbers of our data
print("length of oversampled data is ",len(os_data_X))
print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['y']==0]))
print("Number of subscription",len(os_data_y[os_data_y['y']==1]))
print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_X))
print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_X))

from sklearn.feature_selection import RFE
lr = LogisticRegression()

rfe = RFE(lr,20) # recursive feature elimimation(RFE)
os_data_X = sc.fit_transform(os_data_X)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)