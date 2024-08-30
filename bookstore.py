import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bookstore'
)

cursor = conn.cursor()

query = '''
SELECT books.title, authors.name, books.publication_year, books.genre
FROM books
JOIN authors ON books.author_id = authors.author_id
'''

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}, Genre: {row[3]}')

cursor.close()
conn.close()

