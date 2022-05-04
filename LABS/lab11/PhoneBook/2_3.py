import psycopg2
from config import params

db = psycopg2.connect(**params)

cursor = db.cursor()
def check(name):
    select = '''
            SELECT phone FROM phonebook WHERE name = %s;
    '''
    cursor.execute(select, [name])
    names = cursor.fetchone()
    if names == None: 
        return True
    return False

print("How many people you want to add?")
n = int(input())
for _ in range(0,n):
    name = input()
    number = input()
    city = input()
    if(check(name)): 
        cursor.execute("call inserting(%s, %s, %s);", (name, number, city))
    else:
        cursor.execute("call updating(%s, %s, %s);",(name, number, city))

cursor.close()
db.commit()
db.close()