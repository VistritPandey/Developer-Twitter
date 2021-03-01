import tweepy
auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "CONSUMER KEY SECRET HERE")
auth.set_access_token("ACCESS TOKEN HERE", "ACCESS TOKEN SECRET HERE")
api = tweepy.API(auth)
tweet = input(" ")
api.update_status("your reply", in_reply_to_status_id = tweetid)
print ("Done!")
