import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "registration"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def fetch_all(sql, params=()):
    """SELECT: returns a list of rows."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        conn.close()


def fetch_one(sql, params=()):
    """SELECT: returns one row (or None)."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    finally:
        conn.close()


def execute(sql, params=()):
    """INSERT / UPDATE / DELETE: returns the new id (for INSERT)."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.lastrowid
    finally:
        conn.close()