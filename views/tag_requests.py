from ctypes.wintypes import tagSIZE
import sqlite3
import json
from models import Tag

def get_all_tags():
    """Returns all tags"""

    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER BY label
        """)

        tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)
    
    return tags

def get_single_tag():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER BY label
        """)

        tags = []

        data = db_cursor.fetchone()

        tag = Tag(data['id'], 
                  data['label'])

    
    return tags.__dict__


def create_tag(tag):
    """Adds a new tag to the database"""

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            (label)
        VALUES
            (?)
        """, (tag['label'],))

        id = db_cursor.lastrowid
        tag['id'] = id
    
    return json.dumps(tag)

def update_tag(id, edited_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Tags
            SET
                label = ?
            WHERE id = ?
            """, (edited_tag['label'], id))


        rows_affected = db_cursor.rowcount
        if rows_affected == 0:
            return False
        else:
            return True