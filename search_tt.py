import tweepy
import json
import sys
import re
import datetime

with open("creds/tt.json") as f:
        creds = json.loads(f.read())

access_token = creds["access_token"]
access_token_secret = creds["access_token_secret"]
consumer_key = creds["consumer_key"]
consumer_secret = creds["consumer_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

maxTweets = 200  # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
max_id = None
tweetCount = 0
searchQuery = f"{sys.argv[1]} -filter:retweets"
next_since_id = None

try:
    f = open(f"nextIds/{sys.argv[2]}", "x")
    f.close()
except:
    pass

with open(f"nextIds/{sys.argv[2]}") as f:
    try:
        since_id = int(f.read())
    except:
        since_id = None

today = datetime.date.today().strftime("%Y%m%d")


def remove_pattern(input_txt, pattern):
    return re.sub(pattern, "", input_txt)


def make_search(since_id=None, max_id=None):
    return api.search(
        q=searchQuery,
        lang="pt",
        result_type="recent",
        tweet_mode="extended",
        count=tweetsPerQry,
        since_id=since_id,
        max_id=max_id,
    )


def get_tweet(tweet):
    text = remove_pattern(tweet.full_text, r"@[\w]*")
    text = remove_pattern(text, r"http\S+")
    text = text.replace("\n", "")
    return {
        "name": tweet.user.name,
        "followers": tweet.user.followers_count,
        "tweet": text,
        "tweeted_at": tweet.created_at,
        "retweet_count": tweet.retweet_count,
    }


with open(f"output/{sys.argv[2]}{today}.json", "w") as f:
    while tweetCount < maxTweets:
        try:
            new_tweets = make_search(
                since_id=str(since_id + 1) if since_id else None,
                max_id=str(max_id - 1) if max_id else None,
            )
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(f"{get_tweet(tweet)}\n")

            tweetCount += len(new_tweets)
            max_id = new_tweets[-1].id
            if not next_since_id:
                next_since_id = new_tweets[0].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

with open(f"nextIds/{sys.argv[2]}", "w") as f:
    f.write(f"{next_since_id}")
