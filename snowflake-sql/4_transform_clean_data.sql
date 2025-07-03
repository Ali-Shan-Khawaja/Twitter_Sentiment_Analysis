CREATE OR REPLACE TABLE TweetsCleaned AS
SELECT
    ID,
    LOWER(REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(LANG,
        '@\\w+', ''), -- remove @handles
        'http\\S+', ''), -- remove URLs
        '[^a-zA-Z0-9\\s]', '')) AS cleaned_text, -- remove emojis/special chars
    created_at,
    TEXT AS LANGUAGE,
    author_id,
    topic
FROM TWITTER_PIPELINE.RAW.TWEETS_RAW;