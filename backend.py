import sqlite3 as sql

conn = sql.connect("futurense.db")
cur = conn.cursor()

def userinfo(username):
    cur.execute("SELECT username,password_hash FROM User WHERE username = (?)",(username,))
    value = cur.fetchall()
    return value

# s = input()
# print(checkuser(s)[0])
