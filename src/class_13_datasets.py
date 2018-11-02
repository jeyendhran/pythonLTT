import pandas as pd
import numpy as np

# read data from the given link and change it to dataset
#dfwine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None) # If our csv file has no column header then make header = None
#To set column header
#dfwine.columns = ['Alcohol type', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
 				 #'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

#print(dfwine.head()) # head to return top 5-6 rows
#print(dfwine.iloc[:,1:].values) # To get the data from 1st column as a np array because 0th column is alcohol type


my_df = pd.read_csv("myfile.csv",header=0) # If our csv file has no column header then make header = None
#To set column header
my_df.columns = ['Col1','Col2','Col3','Col4','Col5']
#To set a column as Index number
my_df.set_index('Col5',inplace=True) # inplace to make the changes in the same variable else it will return a new variable

#print(my_df.head())
#print(my_df.iloc[:,:].values) # To get the data from 1st column as a np array because 0th column is header

# pd.Index for creating index object
df = pd.DataFrame(np.arange(12).reshape((6,2)),index=[pd.Index(["A","A","A","B","B","A"],name='state'),pd.Index(["A","A","A","B","B","A"],name='state1')],columns=pd.Index(['evt1','evt2'],name='events'))
#print(df)
# To change the index and columns of dataframe string to lower/upper cases
#print(df.rename(index=str.lower,columns=str.upper))

df = pd.DataFrame(np.arange(12).reshape((6,2)),index=pd.Index(["A","B","C","D","E","F"],name='state'),columns=pd.Index(['evt1','evt2'],name='events'))
#To show columnn wise data
df2 = df.stack()
#print(df2)

# For unstacking there should be no duplicates
#print(df2.unstack())
#print(df2.unstack(0))
#print(df2.unstack('state'))
#print(df2.unstack('events'))

df1 = pd.DataFrame({'key1':['one']*3+['two']*4,
					'key2':[1,1,3,3,3,5,5]})

# Remove duplicates based on (key1,key2)
#print(df1)
#Remove duplcated data from the dict key1 only
#print(df1.duplicated('key1'))
# To remove duplicated data
#print(df1.drop_duplicates())

s1 = pd.Series([1,2,3,3,5])
#Replace one with another
#print(s1.replace([1,2],np.nan))

ages = [20,22,24,25,27,21,23,37,31,61,45,41,43]
bins = [18,25,35,60,100]
grp_names = ['Youth','Adult','MiddleAged','Senior']
#Cut the ages based on ranges from bins grouped by grp_names
# ans = pd.cut(ages,bins,labels=grp_names)
# print(ans)
# print(ans.codes)
# print(pd.value_counts(ans))

data = np.random.rand(20)
#print(pd.cut(data,4,precision=0))
print(pd.qcut(data,4))

df = pd.DataFrame(np.arange(12).reshape((4,3)),index=[pd.Index(["A","A","B","B"],name='state'),pd.Index([1,2,1,2],name='state1')],columns=[['evt1','evt1','evt3'],['d1','d2','d3']])
print(df)
#Another way to give names to Index
df.index.names = ['key1','key2']
df.columns.names = ['Events','Dates']

# print(df)

# print(df.swaplevel('key1','key2'))
#Level number means denotes index number
# print(df.sort_index(level=0))
# print(df.sort_index(level=1))
# print(df.sum(level='key1'))

s = pd.Series([1,np.nan,2,np.nan,5,6])
#print(s.dropna())
df = pd.DataFrame([[1,np.nan,3,np.nan,5,6],[3,4,5,np.nan,7,8],[np.nan,np.nan,np.nan,6,7,8]])

# Drop if any one value in a row in NAN
#print(df.dropna())
# If any set has event one nan then drop it
#print(df.dropna(how='any'))
# If any set has all nan then only drop it
#print(df.dropna(how='all'))
# Drop row with non-NAN values less than thresh value
#print(df.dropna(thresh=4))

#
df = pd.DataFrame({'spices':['Turmeric','Karam Masala', 'Turmeric', 'Karam Masala', 'Pepper powder', 'Turmeric', 'Pepper powder', 'Chilli pepper'],
				'brands':['Pathanjali', 'Everest', 'Sakthi', 'Pathanjali', 'Everest', 'Sakthi', 'Everest', 'Pathanjali'],
				'qty':[2,3,4,6,2,5,1,4],
				'price':[20,40,60,150,60,25,65,55]})

print(df.groupby([df['brands'],df['spices']]).sum())
print(df.groupby([df['brands'],df['spices']]).mean())
print(df.groupby([df['brands']]).size())
print(df.groupby(df.dtypes,axis=1).size())
# for n,g in df.groupby(by='spices'):
# 	print(n)
# 	print(g)
