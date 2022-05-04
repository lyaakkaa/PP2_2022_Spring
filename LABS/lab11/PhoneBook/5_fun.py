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
postgresql_func5 =  '''
        create or replace procedure delete(data varchar)
        as
        $$
            begin
                delete from PhoneBook where name = $1 or phone = $1; 
            end;
        $$ language plpgsql;
    '''
create_proc(postgresql_func5)
