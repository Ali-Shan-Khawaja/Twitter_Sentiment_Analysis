COPY INTO TWEETS_RAW
FROM (
SELECT
    $1:id::STRING as id,
    $1:created_at::TIMESTAMP AS created_at,
    $1:lang::STRING AS lang,
    $1:author_id::STRING AS author_id,
    $1:text::STRING AS text,
    $1:geo AS geo,
     -- Extract topic before the first '20' (start of date)
    SPLIT_PART(
      REGEXP_SUBSTR(METADATA$FILENAME, '[^/]+$'),  -- Get just filename
      '_20', 1
    ) AS topic
  FROM @RAW.TWEET_STAGE
)