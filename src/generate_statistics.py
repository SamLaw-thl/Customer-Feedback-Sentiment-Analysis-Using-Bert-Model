import pandas as pd
import sqlite3

def generate_statistics() -> None:
    """
    Generates statistics on the sentiment distribution of customer feedback.

    This function retrieves all feedback records from the 'feedback' table in the database,
    calculates the distribution of sentiment labels ('positive' or 'negative'), and prints the results.
    """
    conn = sqlite3.connect('customer_feedback.db')
    df = pd.read_sql_query("SELECT * FROM feedback", conn)
    conn.close()

    sentiment_distribution = df[['sentiment']].value_counts()
    print("Sentiment Distribution:")
    print(sentiment_distribution)
