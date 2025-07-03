USE SCHEMA raw_data;

CREATE OR REPLACE TABLE TWEETS_RAW (
  id STRING,
  created_at TIMESTAMP,
  text STRING,
  author_id STRING,
  lang STRING,
  geo VARIANT,
  topic STRING
);

