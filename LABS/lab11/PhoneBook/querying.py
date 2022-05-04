import psycopg2
from config import params
db = psycopg2.connect(**params)

cursor = db.cursor()

cityq = input()

filter = """
    SELECT * FROM Phonebook WHERE city = %s;
"""
cursor.execute(filter,(cityq,))
print(*cursor.fetchall(), sep = '\n')


cursor.close()
db.commit()
db.close()