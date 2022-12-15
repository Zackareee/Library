import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    contents = f.read()
    connection.executescript(contents)

cur = connection.cursor()

cur.execute("INSERT INTO books (id, title, link, read_status) VALUES (?, ?,?,?)",
            ('1', 'Content for the first post', 'https://www.google.com', 0)
            )

cur.execute("INSERT INTO books (id, title, link, read_status) VALUES (?, ?,?,?)",
            ('2', 'One piece', 'https://www.google.com', 1)
            )

connection.commit()
connection.close()
