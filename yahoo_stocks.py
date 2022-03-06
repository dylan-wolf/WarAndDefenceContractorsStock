import yfinance as yf
import pandas as pd
import datetime
from datetime import date

SYMBOLS = ['BAH', 'LMT', 'BA', 'HII', 'LHX']


def getstock(ticker):
    begdate = '2021-1-1'
    enddate = date.today()
    df = yf.download(ticker, start=begdate, end=enddate, )
    df.to_csv("data/{}.csv".format(ticker))

for ticker in SYMBOLS:
    getstock(ticker)
    print(ticker)
    df = pd.read_csv('data/{}.csv'.format(ticker))
    export_list = list(zip(pd.to_datetime((list(df["Date"]))), list(df["Adj Close"])))
    export_df = pd.DataFrame(export_list, columns=['Date', 'Adj Close'])
    export_df.to_csv("data/{}_adj.csv".format(ticker), index=False)



