import sqlite3
from 
connection = sqlite3.connect('database.db')


with open('structure.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, pwd,userrole) VALUES (?, ?,?)",('admin', 'admin123','admin'))
cur.execute("INSERT INTO users (username, pwd,userrole) VALUES (?, ?,?)",('viewer', 'viewer123','viewer'))


connection.commit()
connection.close()