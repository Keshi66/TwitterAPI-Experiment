Twitter API Experiment 🚀
Exploring Tweepy & Twitter API | Faced API Restrictions

"Not every experiment succeeds, but every experiment teaches something." – 📚
❌ The Challenge
I attempted to interact with Twitter's API using Tweepy, but I faced 403 Forbidden errors due to Twitter's new API restrictions. This repository documents my journey, findings, and possible workarounds.

⚡ What Was the Goal?
✅ Authenticate with Twitter API using Tweepy.
✅ Fetch tweets from my home timeline.
✅ Post a tweet programmatically.
✅ Like & retweet posts.

🔻 But due to API access limitations, I was unable to fetch or post tweets with a free-tier API key.

🛑 Issues Faced
❌ 403 Forbidden Error
Error: "You currently have access to a subset of X API V2 endpoints and limited v1.1 endpoints (e.g., media post, oauth) only."

🔍 Why?

Twitter now restricts most API access under the free plan.
The home timeline API (fetching tweets) and posting tweets require a Basic API Access Plan ($100/month).

TweepError Attribute Error
Error: "AttributeError: module 'tweepy' has no attribute 'TweepError'"

🔍 Why?

TweepError was deprecated in newer versions of Tweepy (use tweepy.errors.TweepyException instead).

✅ What Worked
🔹 Successfully authenticated using API keys.
🔹 Retrieved basic user information.
🔹 Learned the limitations of the new Twitter API pricing model.
🔧 Setup & Installation
Want to test it yourself? Follow these steps:

1️⃣ Clone This Repository:
git clone https://github.com/YOUR_USERNAME/Twitter-API-Experiment.git
cd Twitter-API-Experiment
2️⃣ Install Dependencies
pip install tweepy
3️⃣ Run the Script
python twittyapi.py

📌 Key Learnings
💡 API access is not what it used to be!
💡 Tweepy has changed—update your error handling!
💡 Always check API limitations before starting a project.

📢 Final Thoughts
Even though this experiment didn't go as planned, learning from failures is just as important as succeeding! 🧠🔥
If you have any workarounds or suggestions, feel free to contribute! 😊






