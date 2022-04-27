import psycopg2
from config import params
db = psycopg2.connect(**params)

cursor = db.cursor()

name = input()

sql = """
    DELETE FROM PhoneBook WHERE name = %s;
"""

cursor.execute(sql, (name,))

cursor.close()
db.commit()
db.close()

