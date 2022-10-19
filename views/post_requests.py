from dataclasses import dataclass
import sqlite3
import json
from models import Post

def get_all_posts():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.author_name,
            p.category,
            p.date
        FROM posts p
        ORDER BY p.date
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['author_name'], 
                            row['category'], row['date'])

            posts.append(post.__dict__)
    
    return posts