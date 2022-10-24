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
            u.email,
            u.bio,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        ORDER BY username
        """)

        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'], row['username'],row['email'],
            row['bio'], row['password'],row['profile_image_url'],row['created_on'],row['active'])

            users.append(user.__dict__)
    
    return users

def get_single_user(id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.username,
            u.email,
            u.bio,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], 
                    data['first_name'], 
                    data['last_name'], 
                    data['username'], 
                    data['email'],         
                    data['bio'], 
                    data['password'],        
                    data['profile_image_url'],         
                    data['created_on'],
                    data['active'])
    
    return user.__dict__