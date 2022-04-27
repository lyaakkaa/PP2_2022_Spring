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
        cursor.execute(insert, row)
    #        result.append(cursor.fetchone())
# print(result)

cursor.close()
db.commit()
db.close()