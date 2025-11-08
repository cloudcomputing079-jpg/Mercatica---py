import sqlite3

conn = sqlite3.connect('branding.db')
c = conn.cursor()
c.execute('''
CREATE TABLE branding (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT,
    Domain TEXT,
    tagline TEXT,
    colors TEXT,
    logo_ideas TEXT
)
''')
conn.commit()
conn.close()