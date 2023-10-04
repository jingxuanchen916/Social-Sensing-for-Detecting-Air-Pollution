# Retrieve data from mongoDB and store useful information into csv files
# To protect privacy, mongoDB client information is removed

from pymongo import MongoClient
import csv
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

client = MongoClient("")

# # (Sub-Most) Useful
# keywords = ['#Saddleworth air -is:retweet', '#SaddleworthMoor air -is:retweet', '#saddleworthmoorfire air -is:retweet',
#                 '#AirPollution Manchester -is:retweet', '#AirPollution Sheffield -is:retweet', '#Moorlandfire air -is:retweet',
#                 'Saddleworth Air -is:retweet']
# # Relative useful
# keywords = ['manchester air -is:retweet', '#Saddleworth -is:retweet', '#SaddleworthMoor -is:retweet', '#saddleworthmoorfire -is:retweet']
# # Sub-Relative useful
# keywords = ['wildfire air -is:retweet']
#
# # Test OvO
# keywords = ['saddleworth -is:retweet']
# keywords = ['saddleworth fire -is:retweet']

# keywords = ['saddleworth air -is:retweet', '#SaddleworthMoor air -is:retweet',
#                 '#saddleworthmoorfire air -is:retweet', 'saddleworth wildfire -is:retweet']

keywords = ['2021 10-12', '2021 07-09', '2021 04-06', '2021 01-03']

with open('2021_wildfire_air.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'place_id', 'text'])

    for i in keywords:
        tweets = client.Y3_project.Tweets_3.find_one({'query': i})
        for i in tweets['data']:
            try:
                writer.writerow([i['id'], i['created_at'], i['geo']['place_id'], i['text']])
            except:
                writer.writerow([i['id'], i['created_at'], None, i['text']])
