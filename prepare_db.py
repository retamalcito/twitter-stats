import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

import parameters as p


def create_dfs():
    # Source: https://www.kaggle.com/code/prathamsharma123/clean-raw-json-tweets-data
    
    # Read JSON file containing tweets data and removce tweets not in English
    raw_tweets = pd.read_json(p.db_path, lines=True)

    # Normalize 'user' field
    users = json_normalize(raw_tweets['user'])
    users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
    users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)

    # Create DataFrame and remove duplicates
    users = pd.DataFrame(users)
    users.drop_duplicates(subset=['userId'], inplace=True)
    
    # Transform 'raw_tweets' DataFrame
    # Add column for 'userId'
    user_id = []
    for user in raw_tweets['user']:
        uid = user['id']
        user_id.append(uid)
    raw_tweets['userId'] = user_id

    # Remove less important columns
    cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
    tweets = raw_tweets[cols]
    tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)

    # Convert to DataFrame, remove duplicates and keep only English tweets
    tweets = pd.DataFrame(tweets)
    tweets.drop_duplicates(subset=['tweetId'], inplace=True)

    return (users, tweets)


if __name__ == '__main__':
    users, tweets = create_dfs()
    print(users.head(5))
    print(tweets.head(5))
