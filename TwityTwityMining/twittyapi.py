import tweepy
from tweepy import OAuthHandler

print("Starting script...")  # Debugging print

consumer_key = 'cfyxWxMy7LeHR5C7R0nyZ07gB'
consumer_secret = 'F1L2qdbyXmDjpJcsVCeoV23PqzXRn5RvAJ4EExTcURsl9OiwWJ'
access_token = '1905270563700129792-qqSi89rfQnuMuZJ3Yu2jvEKfQIXmmy'
access_secret = 'jo1qnOcZI32yjOFqchNZpRiECoQlAN6QPPpJdqdDqfxxv'

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
