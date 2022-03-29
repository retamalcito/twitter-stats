import pandas as pd


def most_retweets(users, tweets, amount=10):
    by_retweets = tweets.copy()
    by_retweets.sort_values(by=['retweetCount'], inplace=True, ascending=False)

    by_retweets_merged = pd.merge(by_retweets, users, on=['userId'])

    return by_retweets_merged.head(amount)
