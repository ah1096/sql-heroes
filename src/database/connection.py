import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "127.0.0.1", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        message = "failed"
    return message


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as err:
        print(f"The error '{e}' occurred or the hero name is already taken")

        create_connection("postgres", "postgres", "postgres")

        execute_query("""
                    CREATE TABLE something (
                        id serial PRIMARY KEY,
                        num integer,
                        data text)
                    """)

    
            