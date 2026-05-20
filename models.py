import sqlite3

DATABASE = 'database.db'


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    with open('schema.sql', 'r') as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()


def get_posts():
    conn = get_connection()
    posts = conn.execute(
        'SELECT * FROM posts ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    return posts


def add_post(username, content):
    conn = get_connection()
    conn.execute(
        'INSERT INTO posts (username, content) VALUES (?, ?)',
        (username, content)
    )
    conn.commit()
    conn.close()