import psycopg2,csv
from config import params
db = psycopg2.connect(**params)


cursor = db.cursor()
insert = """
    INSERT INTO PhoneBook VALUES(%s, %s, %s) returning *;
"""

with open("phone.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            pass
            #cursor.execute(insert, row)
            #result.append(cursor.fetchone())
try:
    name = input("Enter the name: ")
    phoneNumber = input("Enter the number: ")
    city = input("Enter the city: ")
    cursor.execute(insert, (name,phoneNumber,city))
    print("Successfully added")
except:
    print("This name has already been used, please write another")

cursor.close()
db.commit()
db.close()