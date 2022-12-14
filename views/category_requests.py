import sqlite3
import json
from models import Category

def get_all_categories():
    """Returns all categories"""
    
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
         FROM Categories c
         ORDER By label ASC
        """)

        categories = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return categories

def create_category(category):
    """Adds a new category to the database"""

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            (label)
        VALUES
            (?)
        """, (category['label'],))

        id = db_cursor.lastrowid

        category['id'] = id

    return json.dumps(category)