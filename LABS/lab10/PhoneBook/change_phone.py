import psycopg2
from config import params
db = psycopg2.connect(**params)

cursor = db.cursor()

sql = """
    UPDATE PhoneBook SET phone = %s WHERE name = %s;
"""

name = input()
phone_number = input()

cursor.execute(sql, (phone_number,name))
print("Successfully modified")

cursor.close()
db.commit()
db.close()