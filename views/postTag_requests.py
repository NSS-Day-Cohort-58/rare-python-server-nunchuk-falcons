import sqlite3


import sqlite3
import json

from models.postTags import PostTags

def get_all_post_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute  ("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post_tag = PostTags(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)

    return post_tags

def create_post_tag(new_post_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            ( post_id, tag_id )
        VALUES
            ( ?, ? );
        """, (new_post_tag['post_id'], new_post_tag['tag_id']))

        id = db_cursor.lastrowid

        new_post_tag['id'] = id
    
    return new_post_tag