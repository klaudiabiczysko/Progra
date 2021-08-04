import tweepy
access_token = "type your access token"
access_token_secret = "type your access token secret"
consumer_key = "type your consumer key"
consumer_secret = "type your consumer secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def twitter_query(new_screen_name, new_count):
  statuses = api.user_timeline(screen_name=new_screen_name, count=new_count, tweet_mode='extended', include_rts=False)
  for status in statuses:
      print(f'{status.created_at} \n {status.user.screen_name}: {status.full_text} \n')

if __name__ == "__main__":
  import sys
  from sys import stdin, stderr
  usr_name = sys.argv[1]
  try: # If no second argument is given, 1 is used as the default value for new_count
      chosen_count = sys.argv[2]
  except IndexError:
      chosen_count = 1
  twitter_query(usr_name,chosen_count)
