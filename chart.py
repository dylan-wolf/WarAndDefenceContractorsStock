import plotly.express as px
import pandas as pd


def create_chart():
    df = pd.read_csv('data/weapons_index.csv')
    reversed_df = df.iloc[::-1]
    fig = px.line(reversed_df, x="Date", y="Adj Close", title='Defense Contractors Direct Index')
    fig.show()
    reversed_reddit_df = pd.read_csv('data/mentions_of_war.csv')
    reddit_df = reversed_reddit_df.iloc[:-1]
    fig = px.line(reddit_df, x="Date", y="Mentions of \'War\'", title='Mentions of War on r/News')
    fig.show()


create_chart()

