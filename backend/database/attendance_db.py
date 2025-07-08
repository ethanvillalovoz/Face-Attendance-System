import sqlite3
from datetime import datetime

DB_PATH = "data/attendance.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def mark_attendance_db(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Only mark attendance if not already present for today
    c.execute("SELECT * FROM attendance WHERE name=? AND date(timestamp)=date('now')", (name,))
    if not c.fetchone():
        c.execute("INSERT INTO attendance (name, timestamp) VALUES (?, ?)", (name, now))
        conn.commit()
    conn.close()

def get_attendance_records():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, timestamp FROM attendance ORDER BY timestamp DESC")
    records = c.fetchall()
    conn.close()
    return records