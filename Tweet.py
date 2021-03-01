import tweepy
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)
tweet = input(" ")
api.update_status(status =(tweet))
print ("Done!")
