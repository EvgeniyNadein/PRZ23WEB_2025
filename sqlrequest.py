import sqlite3

db_lp = sqlite3.connect('login_password.db')
cursor_db = db_lp.cursor()
cursor_db.execute('''SELECT * FROM login_password''')
list_logins = cursor_db.fetchall()

for row in list_logins:
    print(row)

cursor_db.close()
db_lp.close()
