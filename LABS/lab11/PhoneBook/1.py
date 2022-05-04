import psycopg2
from psycopg2 import Error
from config import params

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(**params)

    cursor = connection.cursor()
    # хранимая процедура
    cursor.callproc('filter')

    result = cursor.fetchall()
    for row in result:
        print("name = ", row[0])
        print("number = ", row[1])
        print("city = ", row[2])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")