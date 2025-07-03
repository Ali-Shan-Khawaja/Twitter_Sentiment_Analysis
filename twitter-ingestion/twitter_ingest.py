import os
import json
import boto3
import tweepy
from datetime import datetime
from dotenv import load_dotenv
import time

# Load credentials from .env file

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

client = tweepy.Client(bearer_token=BEARER_TOKEN)
session = boto3.Session(profile_name="twitter-project")
s3 = session.client("s3")

# Customize your topics here

TOPICS = ["climate change", "Ozempic", "AI"]
TWEETS_PER_TOPIC = 10  # max = 10 tweets per request

def fetch_tweets(query):
    response = client.search_recent_tweets(
        query=query,
        max_results=TWEETS_PER_TOPIC,
        tweet_fields=["created_at", "lang", "author_id", "text", "geo"],
        expansions=["geo.place_id"],
        place_fields=["full_name", "country", "geo"]
    )
    tweets = [tweet.data for tweet in response.data] if response.data else []
    return tweets

def save_to_s3(data, topic):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    filename = f"raw-tweets/{topic.replace(' ', '_')}_{timestamp}.json"
    
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=json.dumps(data, indent=2),
        ContentType='application/json'
    )
    print(f"✅ Uploaded: {filename}")

def main():
    for topic in TOPICS:
        print(f"Fetching tweets for: {topic}")
        try:
            tweets = fetch_tweets(topic)
            if not tweets:
                print(f"⚠️ No tweets found for topic: {topic}")
                continue
            print(tweets)
            save_to_s3(tweets, topic)
            print(f"✅ Finished topic: {topic}")
            time.sleep(120)
        
        except Exception as e:
            print(f"❌ Error while processing topic '{topic}': {e}")
            continue  # Move to the next topic no matter what

if __name__ == "__main__":
    main()