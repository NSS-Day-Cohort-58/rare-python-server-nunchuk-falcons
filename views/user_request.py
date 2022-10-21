import sqlite3
import json
from models import User

def get_all_users():
    """Returns all users"""

    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.username,
            u.email
        FROM Users u
        ORDER BY username
        """)

        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'], row['username'],row['email'])

            users.append(user.__dict__)
    
    return users