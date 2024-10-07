import customer_feedback_db as cfdb
import generate_statistics as gs
import visualization as v


def main() -> None:
    """
    Runs the customer feedback analysis system.

    This function presents a menu to the user, allowing them to choose from various options:
    1. Show all customer feedbacks stored in the database
    2. Generate statistics
    3. Visualize data
    4. Exit the system
    """
    while True:
        cfdb.create_table()
        print("\nWelcome to the customer feedback anaylsis system")
        print("1. show all customer feedbacks stored in the database")
        print("2. generate statistics")
        print("3. visualization")
        print("4. Exit")

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            cfdb.query_table()
            pass
        elif choice == '2':
            gs.generate_statistics()
        elif choice == '3':
            v.visualize_data()
        elif choice == '4':
            print("Exiting the customer feedback anaylsis system")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()