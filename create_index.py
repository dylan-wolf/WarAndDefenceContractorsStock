import pandas as pd
import numpy as np
from yahoo_stocks import SYMBOLS

def create_index():
    total_adj = np.empty([295])
    for ticker in SYMBOLS:
        df = pd.read_csv('data/{}_adj.csv'.format(ticker))
        new_adj = np.array(df['Adj Close'])
        total_adj += new_adj
    total_adj = total_adj / 5.0
    date_ref_df = pd.read_csv('data/LMT_adj.csv')
    export_list = list(zip(pd.to_datetime((list(date_ref_df["Date"]))), total_adj))
    export_df = pd.DataFrame(export_list, columns=['Date', 'Adj Close'])
    export_df.to_csv("data/weapons_index.csv", index=False)

create_index()