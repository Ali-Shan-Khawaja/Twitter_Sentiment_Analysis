# 🐦 Twitter Sentiment Analysis

A modular data pipeline to extract, transform, and analyze tweet sentiments across topics like **AI**, **Online Shopping**, and **Climate Change**. This project combines real-time ingestion, sentiment scoring, and SQL-based storage for reporting and visualization.



---

## 🚀 Workflow

1. **Tweet Ingestion**  
   - Extracts tweets from Twitter API using AWS Lambda functions.
   - Stores raw JSON files categorized by topic and date.

2. **Sentiment Analysis**  
   - Cleans and processes tweet text.
   - Analyzes sentiment using NLP techniques.
   - Outputs visualizations (word clouds, sentiment scores, etc.).

3. **Data Storage with Snowflake**  
   - Uploads processed data into Snowflake.
   - Scripts available to create and populate necessary tables.

4. **Visualization** *(Optional)*  
   - Final analysis visualized in Power BI or Jupyter Notebooks.

---

## 🧰 Tech Stack

- **Python 3.10+**
- **AWS Lambda**
- **Snowflake SQL**
- **Jupyter Notebooks** *(for testing & EDA)*
- **Power BI** *(optional)*
- **Git/GitHub**

---

## 🔧 Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/Twitter_Sentiment_Analysis.git
   cd Twitter_Sentiment_Analysis

2. **Set up a Virtual Environment**
    python -m venv venv
    source venv/bin/activate   # or venv\Scripts\activate on Windows

3. **Install Dependencies**
    pip install -r sentiment-analysis/requirements.txt
    pip install -r twitter-ingestion/requirements.txt

4. **Configure Secrets**
    Add your API tokens and keys in a .env file.
    Example: twitter-ingestion/.env.example

## 📂 Branches
Branch              Name	                        Purpose
main	            Final version,                  stable code
twitter-ingestion   Scripts for Lambda tweet fetch
sentiment-analysis	Cleaning,                       scoring, visualization
snowflake-sql	    SQL                             scripts for Snowflake staging


## 📈 Sample Topics
The system currently supports sentiment analysis for:

    Artificial Intelligence (AI)
    Online Shopping
    Climate Change
