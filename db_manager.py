import sqlite3
import os
from datetime import datetime

DB_PATH = "database/mindmate.db"

def init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            first_interaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            language_preference TEXT DEFAULT 'english'
        )
    """)
    
    # Mood logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            mood TEXT,
            mood_score INTEGER,
            trigger TEXT,
            message_summary TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    # Conversation history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            mode TEXT,
            user_message TEXT,
            ai_response TEXT,
            detected_emotion TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    # Create default user if not exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (id, name) VALUES (1, 'User')")
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")

def log_mood(user_id, mood, mood_score, trigger, message_summary):
    """Log user's mood"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO mood_logs (user_id, mood, mood_score, trigger, message_summary)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, mood, mood_score, trigger, message_summary))
    conn.commit()
    conn.close()

def log_conversation(user_id, mode, user_message, ai_response, detected_emotion):
    """Log conversation"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO conversations (user_id, mode, user_message, ai_response, detected_emotion)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, mode, user_message, ai_response, detected_emotion))
    conn.commit()
    conn.close()

def get_recent_conversations(user_id, limit=10):
    """Get recent conversation history"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_message, ai_response, detected_emotion, timestamp
        FROM conversations
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
    """, (user_id, limit))
    results = cursor.fetchall()
    conn.close()
    return results

def get_mood_trend(user_id, days=7):
    """Get mood trend for last N days"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT mood, mood_score, timestamp
        FROM mood_logs
        WHERE user_id = ?
        AND timestamp >= datetime('now', '-' || ? || ' days')
        ORDER BY timestamp DESC
    """, (user_id, days))
    results = cursor.fetchall()
    conn.close()
    return results

def get_last_emotion(user_id):
    """Get the last detected emotion for proactive follow-up"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT detected_emotion, timestamp
        FROM conversations
        WHERE user_id = ? AND detected_emotion IS NOT NULL
        ORDER BY timestamp DESC
        LIMIT 1
    """, (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

# Initialize database on import
if not os.path.exists(DB_PATH):
    init_database()
