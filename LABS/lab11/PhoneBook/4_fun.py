import psycopg2
from config import params

def create_func(query):
    try:
        #Connection to db
        db = psycopg2.connect(**params)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

    except (Exception) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if db:
            cursor.close()
            db.close()
            print("Connection with PostgreSQL is closed")

postgresql_func = """
CREATE OR REPLACE FUNCTION pagination(off int, lim int)
RETURNS TABLE(name varchar, phone varchar, city varchar) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM Phonebook offset $1 limit $2;
END;
$$ LANGUAGE plpgsql;
"""
create_func(postgresql_func)