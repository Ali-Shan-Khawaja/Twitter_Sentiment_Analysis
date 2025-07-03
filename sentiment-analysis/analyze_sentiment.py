import os
import pandas as pd
from textblob import TextBlob
from snowflake.connector import connect
from dotenv import load_dotenv
import re

load_dotenv()

# Step 1: Connect to Snowflake
conn = connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

# Step 2: Fetch Raw Tweets
query = "SELECT ID, cleaned_text, topic, created_at FROM TweetsCleaned;"
df = pd.read_sql(query, conn)
df['SENTIMENT_SCORE'] = df['CLEANED_TEXT'].apply(get_sentiment)
df['CREATED_AT'] = pd.to_datetime(df['CREATED_AT'])

# Step 3: Sentiment Score
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Step 4: Create a Table & Write Back to Snowflake
from snowflake.connector.pandas_tools import write_pandas

# Make sure you're using a different table name to avoid overwriting raw data
write_pandas(conn, df[['ID', 'TOPIC', 'CREATED_AT', 'CLEANED_TEXT', 'SENTIMENT_SCORE']], table_name='TweetsScored', auto_create_table=True, use_logical_type=True )

print("✅ Sentiment analysis completed and saved to Snowflake!")
