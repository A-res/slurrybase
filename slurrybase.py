import sqlite3
import csv
import pandas as pd 


conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
#cursor.execute("""CREATE TABLE slurbase
 #                 (title text, country text, rating text)
  #             """)
with open('slurries.csv', newline='') as csvfile:
    df = list(csv.reader(csvfile))
#df = list(pd.read_table("slurries.csv"))
#print (df)
for row in df:
        print(row)
        
cursor.executemany('INSERT INTO slurbase VALUES (?,?,?)', (df))
 
# Сохраняем изменения
conn.commit()

#cursor.executemany("INSERT INTO slurbase VALUES (?,?,?)", slurbase)

       # fwriter.writerow(())

sql = "SELECT * FROM slurbase WHERE title=?"
cursor.execute(sql, [("Strawberry")])
#print(cursor.fetchall())