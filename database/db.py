# database/db.py

import sqlite3
from datetime import datetime

from config import DEBUG

# ==============================
# ⚙️ DATABASE SETTINGS
# ==============================

DB_NAME = "ai_engine.db"


# ==============================
# 🧱 INIT DATABASE
# ==============================

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            reply TEXT,
            source TEXT,
            score INTEGER,
            created_at TEXT
        )
        """)

        conn.commit()
        conn.close()

        if DEBUG:
            print("📦 Database initialized")

    except Exception as e:
        if DEBUG:
            print("❌ DB init error:", e)


# ==============================
# 💾 SAVE DATA
# ==============================

def save_to_db(question, reply, source, score=0):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO logs (question, reply, source, score, created_at)
        VALUES (?, ?, ?, ?, ?)
        """, (
            question,
            reply,
            source,
            score,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

        if DEBUG:
            print("📊 Saved to DB")

    except Exception as e:
        if DEBUG:
            print("❌ DB save error:", e)


# ==============================
# 📊 FETCH DATA (future use)
# ==============================

def fetch_all():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM logs ORDER BY id DESC")
        rows = cursor.fetchall()

        conn.close()
        return rows

    except Exception as e:
        if DEBUG:
            print("❌ DB fetch error:", e)
        return []
