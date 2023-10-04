# Collect required tweets using Twitter API and store them to MongoDB
# To protect privacy, bear token & mongoDB client information is removed

import requests
import json
import time
from datetime import datetime
from pymongo import MongoClient

bearer_token = ''

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
end_time = datetime(2021, 3, 31, 0, 0, 0).isoformat() + "Z"
start_time = datetime(2020, 12, 31, 0, 0, 0).isoformat() + "Z"
query_params = {'max_results': 500, 'end_time': end_time, 'start_time': start_time,
                'user.fields': 'id,username,location,created_at,description',
                'tweet.fields': 'created_at,geo,entities,public_metrics,referenced_tweets'}


# Method required by bearer token authentication.
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


# Get data
def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    # if response.status_code != 200:
    #     raise Exception(response.status_code, response.text)
    result = response.json()
    result['tweets_count'] = response.json()['meta']['result_count']
    result.pop('meta')
    while 'next_token' in response.json()['meta'].keys():
        params['next_token'] = response.json()['meta']['next_token']
        time.sleep(3.1)
        response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
        result['data'].extend(response.json()['data'])
        result['tweets_count'] += response.json()['meta']['result_count']
    # print(result['tweets_count'])
    return result


# connects to mongo db
def connect_to_mongo():
    return MongoClient("")


# send data to mongo db
def send_to_mongo(dbname, dbcollection, data):
    client = connect_to_mongo()
    db = getattr(client, dbname)
    db_collection = getattr(db, dbcollection)
    db_collection.insert_one(data)


# print some tweet's id with its text, create_at, place_id (if tagged) - just for checking
def part_of_tweets(origin_json, num):
    i = 0
    result = {'data': {}}
    while i < min(num, origin_json['tweets_count']):
        temp = {}
        try:
            temp['text'] = origin_json['data'][i]['text']
            temp['created_at'] = origin_json['data'][i]['created_at']
            temp['place_id'] = origin_json['data'][i]['geo']['place_id']
        except:
            pass
        result['data'][origin_json['data'][i]['id']] = temp
        i += 1
    return result


def main():
    # separately tried - Saddleworth Air - datetime(2017/20, 12, 31, 0, 0, 0) - 828 tweets
    # keywords = ['#Saddleworth air -is:retweet', '#SaddleworthMoor air -is:retweet', '#saddleworthmoorfire air -is:retweet',
    #             'Saddleworth Air -is:retweet', '#AirPollution Manchester -is:retweet',
    #             '#AirPollution Sheffield -is:retweet', '#Moorlandfire air -is:retweet']
    # keywords = ['manchester air -is:retweet']
    # keywords = ['#Saddleworth -is:retweet']
    # keywords = ['#SaddleworthMoor -is:retweet']
    # keywords = ['#saddleworthmoorfire -is:retweet']
    # keywords = ['wildfire air -is:retweet']
    # keywords = ['saddleworth -is:retweet']
    # keywords = ['saddleworth wildfire -is:retweet', 'saddleworth air -is:retweet', 'saddleworth smoke -is:retweet']
    # keywords = ['saddleworth fire -is:retweet']
    # keywords = ['saddleworth air -is:retweet', '#SaddleworthMoor air -is:retweet',
    #             '#saddleworthmoorfire air -is:retweet', 'saddleworth wildfire -is:retweet']
    keywords = ['wildfire air -is:retweet']
    count_tweets = {}
    for i in keywords:
        # print(i)
        query_params['query'] = i
        json_response = connect_to_endpoint(search_url, query_params)
        json_response['query'] = '2021 01-03'
        count_tweets[json_response['query']] = json_response['tweets_count']
        # print(json.dumps(part_of_tweets(json_response, 100), indent=4, sort_keys=False))
        # print(json.dumps(json_response, indent=4, sort_keys=False))
        dbname = "Y3_project"
        dbcollection = "Tweets_3"
        send_to_mongo(dbname, dbcollection, dict(json_response))
    print(json.dumps(count_tweets, indent=4))


if __name__ == "__main__":
    main()
