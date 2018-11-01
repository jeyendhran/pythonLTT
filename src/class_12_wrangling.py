import pandas as pd
import numpy as np

df1 = pd.DataFrame({"key1":['a','c','d'],
                   'data1':range(3)})
df2 = pd.DataFrame({"key2":['a','c','a','b','c','c','b'],
                   "data2":range(7)})

#print(pd.merge(df1,df2))
#print(pd.merge(df2,df1,left_on='key2',right_on='key1')) # default join is inner join
#print(pd.merge(df1,df2,left_on='key1',right_on='key2',how='outer')) # how  = outer,inner,left,right

df1 = pd.DataFrame({"st":['TN','KA','TN'],
                    "fg":['pd','wh','pd'],
                   'qty1':[12,34,56]})
df2 = pd.DataFrame({"st":['KA','KA','KL','KL'],
                    "fg":['pd', 'wh', 'pd', 'cn'],
                    "qty2":[7,8,6,8]})

# print(pd.merge(df1,df2,on='st',suffixes=('_1','_2')))
# print(pd.merge(df1,df2,on='fg',suffixes=('_1','_2')))
# print(pd.merge(df1,df2,on=['st','fg']))

df1 = pd.DataFrame({'key':['a','a','b','c','c'],'value':range(5)},index=['a','b','c','d','e'])
df2 = pd.DataFrame({'val':[12,7,6]},index=['a','c','d'])
#print(pd.merge(df1,df2,left_on='key',right_index=True))
#print(pd.merge(df1,df2,left_index=True,right_index=True))

df1 = pd.DataFrame({'key1':['A','B','A','C','D'],'key2':[2000,2000,2001,2000,20002],'data':[3,2,4,4,6]})
df2 = pd.DataFrame(np.arange(12).reshape((6,2)),index=[["A","A","A","B","B","A"],[2000,2001,2002,2000,2000,2002]],columns=['evt1','evt2'])
#print(pd.merge(df1,df2,left_on=['key1','key2'],right_index=True))
#print(pd.merge(df2,df1,right_on=['key1','key2'],left_index=True))

arr = np.arange(12).reshape(3,4)
# print(arr)
# print(np.concatenate([arr,arr]))

s1 = pd.Series([1, 3], index=['a', 'b'])
s2 = pd.Series([4, 3, 2], index=['a', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
# print(pd.concat([s1, s2, s3],sort=True,join='inner'))
# print(pd.concat([s1, s2, s3], axis=1,sort=True))


a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
#print(np.where(pd.isnull(a), b, a))
#print(b[:-2],a[2:])
print(b[:-2].combine_first(a[2:]))
