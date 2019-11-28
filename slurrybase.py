import sqlite3

conn = sqlite3.connect('slurries.db')


#cursor.execute("""CREATE TABLE rslurries(title text,country text,ratings real)""")
#cursor.execute("""INSERT INTO rslurries VALUES ('test', 'russia', '0/0')""")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
 
sql = "SELECT * FROM rslurries WHERE title='test'"
cursor.execute(sql)
print(cursor.fetchall()) # or use fetchone()
 
print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM rslurries ORDER BY title"):
    print(row)
 
print("Results from a LIKE query:")
sql = "SELECT * FROM rslurries WHERE title LIKE 'test'"
cursor.execute(sql)
 
print(cursor.fetchall())
#for row in cursor.execute(sql):
   

#conn.commit

#https://python-scripts.com/sqlite