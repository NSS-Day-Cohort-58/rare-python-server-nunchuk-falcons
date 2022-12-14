from dataclasses import dataclass
import sqlite3
import json
from models import Post, Category, User

def get_all_posts():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url user_image,
            u.created_on user_created_date,
            u.active user_active,
            c.id category_id,
            c.label category_label
        FROM posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        ORDER BY p.publication_date DESC
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], 
                            row['title'], row['publication_date'], row['image_url'],
                            row['content'], row['approved'])
            
            user = User(row['user_id'], row['user_first_name'], row['user_last_name'], row['user_username'], row['user_email'], row['user_bio'], row['user_password'], row['user_image'], row['user_created_date'], row['user_active'])

            category = Category(row['category_id'], row['category_label'])

            post.user = user.__dict__
            post.category = category.__dict__
            posts.append(post.__dict__)
    
    return posts


def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url user_image,
            u.created_on user_created_date,
            u.active user_active,
            c.id category_id,
            c.label category_label
        FROM posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = Post(data['id'], 
                    data['user_id'], 
                    data['category_id'], 
                    data['title'], 
                    data['publication_date'],         
                    data['image_url'],         
                    data['content'],         
                    data['approved'])
        
        user = User(data['user_id'], 
                    data['user_first_name'], 
                    data['user_last_name'], 
                    data['user_username'], 
                    data['user_email'], 
                    data['user_bio'], 
                    data['user_password'], 
                    data['user_image'], 
                    data['user_created_date'], 
                    data['user_active'])

        category = Category(data['category_id'], data['category_label'])

        post.user = user.__dict__
        post.category = category.__dict__
    
    return post.__dict__

def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO posts
            ( user_id, category_id, title, publication_date, image_url, content, approved)
        VALUES
            ( ?, ?, ?, ?, ?, ?, ? )
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], 
                new_post['publication_date'], new_post['image_url'], 
                new_post['content'], new_post['approved']))
        
        id = db_cursor.lastrowid

        new_post['id'] = id
    
    return json.dumps(new_post)

def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))

def update_post(id, edited_post):
    """Updates a post"""

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (edited_post['user_id'], 
                edited_post['category_id'], 
                edited_post['title'], 
                edited_post['publication_date'],
                edited_post['image_url'], 
                edited_post['content'], 
                edited_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True
