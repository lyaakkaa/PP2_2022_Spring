#Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

import psycopg2
from psycopg2 import Error
from config import params


def create_func(query):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


postgresql_func = """
CREATE OR REPLACE FUNCTION filter()
  RETURNS TABLE(name varchar, phone varchar, city varchar) AS $$
BEGIN
 RETURN QUERY
 SELECT * FROM Phonebook where Phonebook.phone LIKE '8747%' ;
END;
$$ LANGUAGE plpgsql;
"""
create_func(postgresql_func)


# postgresql_func = """
# DROP FUNCTION filter(max_price integer)
# """