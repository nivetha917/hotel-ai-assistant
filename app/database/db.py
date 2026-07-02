import sqlite3

# Database file name
DB_NAME = "hotel.db"


def get_connection():
    """
    Create and return a connection to the SQLite database.
    If hotel.db does not exist, SQLite creates it automatically.
    """
    return sqlite3.connect(DB_NAME)


def create_tables():
    """
    Create the reservations table if it does not already exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (

            reservation_id TEXT PRIMARY KEY,

            guest_name TEXT NOT NULL,

            email TEXT NOT NULL,

            check_in TEXT NOT NULL,

            check_out TEXT NOT NULL,

            room_type TEXT NOT NULL,

            status TEXT NOT NULL

        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_tables()

    print("Database created successfully!")