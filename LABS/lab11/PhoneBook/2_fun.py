import psycopg2
from config import params

def create_proc(query):
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
#insert:
# postgresql_func1 = """
# DROP PROCEDURE inserting"""
# postgresql_func2= """
# DROP PROCEDURE updating"""
postgresql_func1 = """
    create or replace procedure inserting(name varchar, phonenumber varchar, city varchar)
    as
    $$
        begin
            insert into Phonebook(name, phone, city) values ($1, $2, $3);
        end; 
    $$ 
    language plpgsql;  
"""
postgresql_func2 = """
    create or replace procedure updating(name varchar, n_phone varchar, city varchar)
    as
    $$
        begin
            UPDATE Phonebook 
            SET phone = $2, city = $3
            WHERE PhoneBook.name = $1;
        end; 
    $$ 
    language plpgsql;  
"""
create_proc(postgresql_func1)
create_proc(postgresql_func2)