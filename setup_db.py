import sqlite3

conn = sqlite3.connect('branding.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS branding_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        brand TEXT,
        domain TEXT,
        font TEXT,
        colors TEXT,
        logo_prompt TEXT,
        domain_name TEXT,
        languages TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

print("✅ branding_history table created successfully.")