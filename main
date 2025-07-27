import feedparser
import tweepy
import os

# 🔐 環境変数からAPIキーを読み込む（GitHubの秘密設定に保存する予定）
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# 🐤 Twitter認証
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 📰 YahooニュースRSSから記事を取得
feed = feedparser.parse("https://news.yahoo.co.jp/rss/topics/top-picks.xml")
entry = feed.entries[0]  # 一番上の記事を使う

# 📝 ツイート文を作って投稿
tweet = f"{entry.title}\n{entry.link}"
api.update_status(tweet)
