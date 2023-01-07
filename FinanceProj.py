import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.Ticker('PETR4.SA').history(period = 'max')

df.head()
print (df.head())

df.head(n=2)
print(df.head(n=2))

df.head(n=3)
print(df.head(n=3))

df.info()
print (df.info())

df.dtypes
print(df.dtypes)

df.shape
print(df.shape)

df.describe().T
print(df.describe().T)

df.loc['2020-11-1':'2020-12-31', ['Open','Close']]
print(df.loc['2020-11-1':'2020-12-31', ['Open','Close']])

df[df['Open'] > 32.95]
print(df[df['Open'] > 32.95])

df[(df['Open']>=30) & (df['High']>33.5)]
print(df[(df['Open']>=30) & (df['High']>33.5)])

df[(df['Close']>32.8) & (df['Close']<33)]
print(df[(df['Close']>32.8) & (df['Close']<33)])

df[(df['High']<7) | (df['Low']<9)]
print(df[(df['High']<7) | (df['Low']<9)])



