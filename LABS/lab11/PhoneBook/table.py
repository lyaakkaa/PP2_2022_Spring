import psycopg2
from config import params

db = psycopg2.connect(**params)
cursor = db.cursor()

cursor.execute('''CREATE TABLE PhoneBook(
     name VARCHAR(255) PRIMARY KEY,
     phone VARCHAR(255),
     city VARCHAR(255)
);''')

#drop_table = '''DROP TABLE PhoneBook'''
#cursor.execute(drop_table)

cursor.close()
db.commit()
db.close()
