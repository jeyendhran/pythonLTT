import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
from _datetime import datetime
from datetime import timedelta

start = datetime(2011, 1, 7)
print(str(start))
print(start.strftime('%Y-%m-%d'))

start = '2011-01-23'
print(datetime.strptime(start, '%Y-%m-%d'))

start = datetime(2011, 1, 7)
print(start + timedelta(12))
print(start - timedelta(24))

start = ['7/6/2011', '8/6/2011']
print([datetime.strptime(x, '%m/%d/%Y') for x in start])

now = datetime.now()
print(now.time(),now.year,now.month,now.day)
delta = datetime(now.year,now.month,now.day) - datetime(1995, 10, 4)
print(delta)

print(parse('2011-01-03'))
print(parse('Jan 31, 1997 10:45 PM'))

print(pd.to_datetime(start))
idx = pd.to_datetime(start + [None])
print(pd.isnull(idx))

ts = pd.Series(np.random.randn(6),index = pd.date_range('1/11/2011',periods=6,freq='D'))
print(ts)
print(ts.shift(2))
print(ts/ts.shift(1)-1)
ts = ts.tz_localize('UTC')
print(ts)
print(ts.tz_convert('GMT'))

#index_col is 0th column so index_col = 0
# stocks = pd.read_csv("stock_px.csv",parse_dates=True,index_col=0)
# stock = stocks[['AAPL','MSFT']]
# print(stock)
# #stock.plot()
# #Plot for a range of dates
# #stock.loc['13-02-2003':'20-06-2003'].plot()
# #rolling 250 means calc mean for every 250th data
# stock.MSFT.rolling(250).mean().plot()

stocks = pd.read_csv("NIFTY-I.csv",header=None)
stocks.columns = ['date','time','open','high','low','close','volumn','OI']
stocks['period'] = stocks['date'].map(str) + stocks['time']
stocks.drop(axis=1,columns=['date','time'],inplace=True)
stocks['period'] = pd.to_datetime(stocks['period'],format='%Y%m%d%H:%M')
stocks.set_index('period',inplace=True)
print(stocks.head())
stocks.plot()
plt.show()
