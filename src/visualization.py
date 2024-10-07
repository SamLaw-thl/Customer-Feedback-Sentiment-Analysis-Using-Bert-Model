import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import pandas as pd

def visualize_data() -> None:
    """
    Generates a bar plot to visualize the sentiment distribution of customer feedback.

    This function retrieves all feedback records from the 'feedback' table in the database,
    creates a count plot showing the distribution of sentiment labels ('positive' or 'negative'),
    and displays the plot.
    """
    conn = sqlite3.connect('customer_feedback.db')
    df = pd.read_sql_query("SELECT * FROM feedback", conn)
    conn.close()

    plt.figure(figsize=(10, 6))
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.show()

