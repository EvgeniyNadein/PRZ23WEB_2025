import sqlite3


db_lp = sqlite3.connect('login_password.db')
cursor_db = db_lp.cursor()
cursor_db.execute('''CREATE TABLE IF NOT EXISTS login_password(login TEXT PRIMARY KEY, password TEXT NOT NULL)''')
db_lp.commit()
cursor_db.close()
db_lp.close()
