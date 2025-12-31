# database.py
# Simple database connection simulation for Lab 6

def connect_to_database():
    try:
        # Simulated database credentials
        db_name = "lab_database"
        user = "admin"
        password = "admin123"

        # Simulated connection logic
        if user == "admin" and password == "admin123":
            print(f"Connected successfully to {db_name}")
            return True
        else:
            raise ConnectionError("Invalid database credentials")

    except ConnectionError as error:
        print("Database connection failed:", error)
        return False


def main():
    status = connect_to_database()
    if status:
        print("Database operations can proceed.")
    else:
        print("Please check database settings.")


if __name__ == "__main__":
    main()

