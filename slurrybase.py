import sqlite3
import csv

conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
#cursor.execute("""CREATE TABLE slurbase
 #                 (title text, country text, rating text)
  #             """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO slurbase
                   VALUES ('Strawberry', 'Russia', '7/10')"""
              )
 
# Сохраняем изменения
conn.commit()

#cursor.executemany("INSERT INTO slurbase VALUES (?,?,?)", slurbase)
conn.commit()

sql = "SELECT * FROM slurbase WHERE title=?"
cursor.execute(sql, [("Strawberry")])
print(cursor.fetchall())