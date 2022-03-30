import pandas as pd


def most_active_users(users, tweets, amount=10):
    tweets_merged = pd.merge(tweets, users, on=['userId'])
    user_count = tweets_merged.groupby(['username'])['username'].count().reset_index(name='count')

    user_count.sort_values('count', inplace=True, ascending=False)

    return user_count.head(amount)
