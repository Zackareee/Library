import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    contents = f.read()
    connection.executescript(contents)

cur = connection.cursor()

cur.execute("INSERT INTO books (id, title) VALUES (?, ?)",
            ('1', 'Content for the first post')
            )

cur.execute("INSERT INTO books (id, title) VALUES (?, ?)",
            ('2', 'Content for the second post')
            )

connection.commit()
connection.close()
