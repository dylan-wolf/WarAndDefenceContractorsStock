import datetime
from datetime import date
from datetime import datetime as dt
import pandas as pd
from psaw import PushshiftAPI

api = PushshiftAPI()

start_time = int(datetime.datetime(2021, 1, 2).timestamp())
end_date = date.today()

submissions = api.search_submissions(after=start_time,
                                     before=end_date,
                                     subreddit='news',
                                     filter=['url', 'author', 'title', 'subreddit'])
my_dates = {}


def print_war():
    for submission in submissions:

        words = submission.title.split()
        wartags = list(filter(lambda word: word.lower() == 'war' or word.lower() == 'wars', words))
        t = submission.created_utc
        string_dates = str(dt.utcfromtimestamp(t))[:-9]

        if len(wartags) > 0:
            if string_dates in my_dates:
                my_dates[string_dates] += len(wartags)
            else:
                my_dates[string_dates] = 1
                print(string_dates)


print_war()

for date, amount in my_dates.items():
    print("War was mentioned " + str(amount) + " times on " + date)

df = pd.DataFrame(list(my_dates.items()), columns=['Date', 'Mentions of \'War\''])
print(df.head())
df.set_index("Date", inplace=True)
df.to_csv('data/mentions_of_war.csv', mode='a')
