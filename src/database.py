import sqlite3, json
from datetime import datetime

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY, 
            timestamp TEXT, 
            mode TEXT, 
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_session(mode, codes, db_file):
    ts = datetime.now().isoformat()
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(
        'INSERT INTO sessions (timestamp, mode, data) VALUES (?,?,?)',
        (ts, mode, json.dumps(codes))
    )
    session_id = c.lastrowid
    conn.commit()
    conn.close()
    return session_id

def fetch_history(db_file, limit=50):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(
        'SELECT id, timestamp, mode, data FROM sessions '
        'ORDER BY timestamp DESC LIMIT ?',
        (limit,)
    )
    rows = c.fetchall()
    conn.close()
    return [
        {'id':r[0], 'timestamp':r[1], 'mode':r[2], 'codes':json.loads(r[3])}
        for r in rows
    ]
