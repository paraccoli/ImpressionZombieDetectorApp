import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from collections import Counter

def get_twitter_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def detect_imprezombies(api, username, threshold, tweet_count=100):
    zombies = []
    tweets = api.user_timeline(screen_name=username, count=tweet_count)

    for tweet in tweets:
        if tweet.retweeted or tweet.in_reply_to_status_id:
            continue

        likers = api.get_favorites(id=tweet.id, count=100)
        retweeters = api.get_retweeters(id=tweet.id)

        interacters = Counter([user.screen_name for user in likers + list(retweeters)])

        for user, count in interacters.items():
            if count / len(tweets) > threshold:
                zombies.append(user)

    return list(set(zombies))