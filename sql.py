import sqlite3

DATABASE = "blog.db"

def create_db_and_populate():
    try:
        with sqlite3.connect(DATABASE) as connection:
            c = connection.cursor()
            c.execute(
                        """
                        CREATE TABLE posts
                        (
                            title TEXT,
                            post TEXT
                        )
                        """
                      )

            dummy_data = [
                ("Good", "I'm good."),
                ("Well", "I'm well."),
                ("Excellent", "I'm excellent."),
                ("Okay", "I'm okay.")
                ]
            # Insert dummy data into the table
            c.executemany("INSERT INTO posts VALUES (?, ?)", dummy_data)
    except Exception as e:
        print(e)

create_db_and_populate()

