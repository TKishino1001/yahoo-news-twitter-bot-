import feedparser
import tweepy
import os

# Twitter API v2 ベアラートークン認証
client = tweepy.Client(
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

# Yahooニュース RSSを取得
feed = feedparser.parse("https://news.yahoo.co.jp/rss/topics/top-picks.xml")
entry = feed.entries[0]  # 一番上の記事だけ

# ツイートを投稿（v2方式）
tweet = f"{entry.title}\n{entry.link}"
response = client.create_tweet(text=tweet)

print("✅ Tweeted:", response)
