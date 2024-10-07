import sqlite3


def create_table() -> None:
    """
    Creates an SQLite table to store customer feedback.

    This function establishes a connection to the 'customer_feedback.db' database,
    creates a table named 'feedback', and defines its columns for storing feedback data.
    """
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback(
                   id INTEGER PRIMARY KEY, 
                   comment TEXT,
                   sentiment TEXT
                   )
                   ''')

    conn.commit()
    conn.close()


def query_table() -> None:
    """
    Queries all records from the 'feedback' table in the 'customer_feedback.db' database.

    This function retrieves all feedback records from the database and prints them to the console.
    """
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM feedback')
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    if rows:
        for row in rows:
            print(row)
    else:
        print("There is no customer feedback stored")

