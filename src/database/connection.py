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


#=================PUT FUNCTIONS AND WHATNOT VVV HERE VVV UNTIL JOSH FIGURES STUFF OUT, DO NOT EDIT ABOVE=======


#=============save this bit of code for the View Hero function
def select_all():
    query = """
        SELECT * from heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    print(list_of_heroes)
    for record in list_of_heroes:
        print(record[1])

select_all()
#=================================================================================





#CREATE===========================================================================
def add_hero(add_name, add_about_me, add_biography):
    add_name = input("What is your hero name? ")
    add_about_me = input("Write a short tagline, fun fact about yourself, or your motto: ")
    add_biography = input("What is your origin story? ")
    #add_abilities = input("What powers do you have? ")

    print(add_name, add_about_me, add_biography)
    confirm_add = input(f"Would you like to add {add_name}'s profile? Enter [YES] to confirm, or [NO] to start over.")
    if confirm_add == "YES":
        print(f"{add_name}'s profile has been created.")
        query = ("""
                    INSERT INTO heroes (name, about_me, biography)
                    VALUES (add_name, add_about_me, add_biography)
                """)
        execute_query(query,(add_name, add_about_me, add_biography))
    else:
        #return to menu
        print("return to menu; this text is here so Python doesn't get mad")

#READ=============================================================================
def view_hero(hero_to_view):
    view_choice = input("Input a specific hero name, or enter [A] to see all hero profiles")

    if view_choice == "A":
        #show all profiles with bit of code @ top ?????????
        print("show all; this text is here so Python doesn't get mad")
    else:
        #show only hero_to_view's profile ??????????
        print("show profile; this text is here so Python doesn't get mad")


#UPDATE===========================================================================
def update_profile(hero_to_update, updated_name, updated_about_me, updated_biography):
    hero_to_update = input("Type the name of the hero whose profile you wish to UPDATE: ")
    print(f"You have chosen to update {hero_to_udate}'s profile. Type [NO CHANGE] for profile aspects that you wish to remain unchanged.")
    
    updated_name = input(f"Change {hero_to_update}'s name to: ")
    if updated_name == "NO CHANGE":
        #do nothing??
        print("do nothing; this text is here so Python doesn't get mad")
    else:
        query = (""" 
                    UPDATE heroes
                    SET name = updated_name
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_name))

        #might need to change hero_to_update to the hero's id because if name is changed, other conditionals
        #that depend on the name value will not work; ask for help

    updated_about_me = input(f"Change {hero_to_update}'s about me to: ")
    if updated_about_me == "NO CHANGE":
        #do nothing??
        print("do nothing; this text is here so Python doesn't get mad")
    else:
        query = (""" 
                    UPDATE heroes
                    SET about_me = updated_about_me
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_about_me))
    
    updated_biography = input(f"Change {hero_to_update}'s biography to: ")
    if updated_biography == "NO CHANGE":
        #do nothing??
        print("do nothing; this text is here so Python doesn't get mad")
    else:
        query = (""" 
                    UPDATE heroes
                    SET biography = updated_biography
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_biography))


#keep this code just in case

    #("""
        #UPDATE heroes
        #SET name = updated_name,
            #about_me = update_about_me,
            #biography = updated_about_me
        #WHERE name = hero_to_update)
    #""")


#DELETE==========================================================================
def delete_hero(hero_to_delete):
    hero_to_delete = input('Type the name of the hero whose profile you wish to DELETE: ')
    pollice_verso = input(f'Are you sure you want to delete {hero_to_delete}? Enter [YES] or [NO]: ')
    
    if pollice_verso == "YES":
        print(f"{hero_to_delete} has been deleted")
        query = ("""
                    DELETE FROM heroes WHERE name = hero_to_delete
                """)
        execute_query(query,(hero_to_delete))
        #return to menu -> figure out when done with menu function
    elif pollice_verso == "NO":
        cold_feet = input("Would you like to delete a different hero [DEL], or return to the menu [M]?")
        if cold_feet == "DEL":
            delete(hero)
        elif cold_feet == "M":
            #return to menu
            print("return to menu; this text is here so Python doesn't get mad")

#MENU============================================================================

user = input("Welcome to SuperBase. Log in as:")

def menu():
    what_do = input(f"Hello, {user}. What would you like to do?" + '\n' +
                            "[1] ADD hero profile" + '\n' +
                            "[2] VIEW hero profile(s)" + '\n' +
                            "[3] UPDATE hero profile(s)" + '\n' +
                            "[4] DELETE hero profile(s)")

menu()
