import tweepy
from tweepy import OAuthHandler

print("Starting script...")  # Debugging print

consumer_key = 'your api key'
consumer_secret = 'your api secret key'
access_token = 'your access token'
access_secret = 'your access secret token'

try:
    # 🔹 Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # 🔹 Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # 🔹 Verify Authentication
    user = api.verify_credentials()
    if user:
        print(f"✅ Authentication successful! Logged in as: {user.screen_name}")
    else:
        print("❌ Authentication failed! Check your API keys.")

except tweepy.errors.TweepyException as e:  # ✅ Corrected Exception Handling
    print(f"❌ Tweepy Error: {e}")

'''# 🔹 Instead of `home_timeline()`, fetch your own tweets (Allowed in Free API)
try:
    print("\nFetching your recent tweets...\n")
    tweets = api.user_timeline(count=5)
    
    for tweet in tweets:
        print(tweet.text)

except tweepy.errors.TweepyException as e:
    print(f"❌ Error fetching tweets: {e}")
'''
# 🔹 Post a Tweet (Allowed in Free API)
try:
    api.update_status("Hello Twitter! This is my first tweet using Tweepy! 🚀")
    print("\n✅ Tweet posted successfully!")

except tweepy.errors.TweepyException as e:
    print(f"❌ Error posting tweet: {e}")
