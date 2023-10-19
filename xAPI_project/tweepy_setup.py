import tweepy
import requests

api_key = "WmmTySByCwfqKbrZyhFMrXu5m"
api_key_secret = "8mXe60hJWqmoymrkIi4goniDwK3ltOOTvJFBsbcGikky13KbNL"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAD%2FOpgEAAAAAwVwSJ5wZGCFuSwtyY6WOvkXspL4%3DAIUMvTUwPZu4nIfXqedQLvSGNFc4SnEOYXD1jyGmofdibmklPm"
access_token = "1001708151048204288-n6kO8xK3zICvcB3QjW8w9rnEqMNYnp"
access_token_secret = "WYlUoEo9mIL04z4yaXfqKsuNbyNgSnkufaI41vWUsTbAw"

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text="Tweet via API")
