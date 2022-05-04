import psycopg2
from config import params
db = psycopg2.connect(**params)

cursor = db.cursor()

sql = """
    UPDATE PhoneBook SET city = %s WHERE name = %s;
"""

name = input()
city = input()

cursor.execute(sql, (city,name))
print("Successfully modified")

cursor.close()
db.commit()
db.close()