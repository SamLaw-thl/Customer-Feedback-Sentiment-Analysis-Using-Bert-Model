import tkinter as tk
from tkinter import messagebox
import sqlite3
import sentiment_analysis_model as sa


def submit_comment() -> None:
    """
    Handles the submission of customer comments.

    This function retrieves the comment entered by the user in the GUI,
    saves it using the 'save_comment' function, and provides appropriate
    feedback to the user via message boxes.
    """
    comment = comment_entry.get("1.0", tk.END).strip()
    if comment:
        save_comment(comment)
        comment_entry.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Comment submitted successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter a comment.")


def save_comment(comment: str) -> None:
    """
    Saves a customer comment along with its sentiment analysis result to the database.

    This function analyzes the sentiment of the given comment using an external sentiment analysis tool,
    and then inserts the comment and its sentiment into the 'feedback' table in the database.

    Args:
        comment (str): The customer's comment.
    """
    sentiment_result = sa.analyze_sentiment(comment)
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (comment, sentiment) VALUES (?, ?)", (comment, sentiment_result))
    conn.commit()
    conn.close()


# Tkinter setup
root = tk.Tk()
root.title("Customer Feedback")

tk.Label(root, text="Leave your comment:").pack()
comment_entry = tk.Text(root, height=10, width=50)
comment_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_comment)
submit_button.pack()


root.mainloop()
