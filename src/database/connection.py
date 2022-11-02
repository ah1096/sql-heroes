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
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")


#PUT FUNCTIONS AND WHATNOT VVV HERE VVV UNTIL JOSH FIGURES STUFF OUT, DO NOT EDIT ABOVE


#save this bit of code for the View Hero function
#def select_all():
    #query = """
        #SELECT * from heroes
    #"""

    #list_of_heroes = execute_query(query).fetchall()
    #print(list_of_heroes)
    #for record in list_of_heroes:
        #print(record[1])

#select_all()

#add abilities to this function later!!!!!!!!!!!!
def add_hero(add_name, add_about_me, add_biography):
    add_name = input("What if your hero name? ")
    add_about_me = input("Write a short tagline, fun fact about yourself, or your motto: ")
    add_biography = input("What is your origin story? ")
    #add_abilities = input("What powers do you have? ")

    ("""
        INSERT INTO heroes (name, about_me, biography)
        VALUES (add_name, add_about_me, add_biography)
    """)

def delete_hero(deleted_hero):
    deleted_hero = input('Type the name of the hero whose profile you wish to DELETE: ')
    ("""
        DELETE FROM heroes WHERE name = deleted_hero
    """)

#ask for help on this function
def update_profile(hero_to_update, updated_name, updated_about_me, updated_biography):
    hero_to_update = input("Type the name of the hero whose profile you wish to UPDATE: ")
    updated_name = input(f"Change {hero_to_update}'s name to: ")
    updated_about_me = input("Change this hero's about me to: ")
    updated_biography = input("Change this hero's biography to: ")
    ("""
        UPDATE heroes
        SET name = updated_name)
    