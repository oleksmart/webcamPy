import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

""" cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
result = cursor.fetchall()
print(result)

cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
result = cursor.fetchall()
print(result)

# Insert new rows
new_rows = [('Dogs', 'Dog City', '2099.10.15'), ('Cats', 'Cat City', '2077.10.15')]

cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
connection.commit()
 """



""" cursor.execute("DELETE FROM events")

# Commit the changes to the database
connection.commit() """





cursor.execute("SELECT * FROM events")
result = cursor.fetchall()
print(result)
