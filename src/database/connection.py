import psycopg
from psycopg import OperationalError
from os import system, name
from time import sleep

#for clearing the terminal; see README for link to documentation:
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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
        #print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        #print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")





#=============save this bit of code for the View Hero function
def select_all():
    query = """
        SELECT name from heroes
    """
    list_of_heroes = execute_query(query).fetchall()
    #print(f"""{list_of_heroes}""" + '\n')
    for record in list_of_heroes:
        print(f""" {record[0]}""")

#✅MENU==================================================================================
def menu():
    what_do = str(input(f"What would you like to do?" + '\n' +
                            "[1] ADD hero profile" + '\n' +
                            "[2] VIEW hero profile(s)" + '\n' +
                            "[3] UPDATE hero profile(s)" + '\n' +
                            "[4] DELETE hero profile(s)"))
    if what_do == "1":
        clear()
        add_hero()
    elif what_do == "2":
        clear()
        view_hero()
    elif what_do == "3":
        clear()
        update_profile()
    elif what_do == "4":
        clear()
        delete_hero()


#✅CREATE===========================================================================
def add_hero(add_name=None, add_about_me=None, add_biography=None):
    add_name = input("Input hero name: ")
    add_about_me = input("Input hero tagline, catchphrase, or motto: ")
    add_biography = input("Input hero origin story/biography: ")
    #add_abilities = input("What powers do you have? ")

    print(add_name, add_about_me, add_biography)
    confirm_add = input(f"Would you like to add {add_name}'s profile? Enter [YES] to confirm, or [NO] to start over.")
    if confirm_add == "YES" or "yes" and len(confirm_add)==3:
        print(f"{add_name}'s profile has been created.")
        query = ("""
                    INSERT INTO heroes (name, about_me, biography)
                    VALUES (%s, %s, %s)
                """)
        execute_query(query,(add_name, add_about_me, add_biography))
        sleep(3)
        clear()
        menu()
    elif confirm_add == "NO" or "no" and len(confirm_add)==2:
        print(f"Starting over.....")
        sleep(3)
        clear()
        add_hero()
        


#✅READ=============================================================================
def view_hero():
    hero_to_view = input("Input a specific hero name, or enter [A] to see all hero profiles: ")
    def show_one_profile(hero_name):
            query = """
                    SELECT * from heroes
                    WHERE name = %s
                    """
            single_hero = execute_query(query, (hero_name,)).fetchone()
            print(f"""{single_hero[1]}: 
                    {single_hero[2]}
                    {single_hero[3]} """)
    if hero_to_view == "A" or "a" and len(hero_to_view)==1:
        select_all()
        return_to_menu = input("Type [M] to return to the menu, or enter a hero's name to view their profile: ")
        if return_to_menu == "M" or "m" and len(return_to_menu)==1:
            clear()
            menu()
        else:
            show_one_profile(return_to_menu)
            return_to_menu = input("Type [M] to return to the menu: ")
            if return_to_menu == "M" or "m" and len(return_to_menu)==1:
                clear()
                menu()
        

#UPDATE===========================================================================
def update_profile(hero_to_update=None, updated_name=None, updated_about_me=None, updated_biography=None):
    hero_to_update = input("Type the name of the hero whose profile you wish to UPDATE: ")
    print(f"You have chosen to update {hero_to_update}'s profile. Type [NO CHANGE] for profile aspects that you wish to remain unchanged.")
    updated_name = input(f"Change {hero_to_update}'s name to: ")
    if updated_name == "NO CHANGE":
        #do nothing??
        print(f"{updated_name}do nothing; this text is here so Python doesn't get mad")
    else:
        query = ("""
                    UPDATE heroes
                    SET name = %s
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_name,))

        print(f"{updated_name} -> change name; fillertext")

        #might need to change hero_to_update to the hero's id because if name is changed, other conditionals
        #that depend on the name value will not work; ask for help

    updated_about_me = input(f"Change {hero_to_update}'s about me to: ")
    if updated_about_me == "NO CHANGE":
        #do nothing??
        print(f"{updated_about_me}; do nothing; this text is here so Python doesn't get mad")
    else:
        query = (""" 
                    UPDATE heroes
                    SET about_me = %s
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_about_me,))

        print(f"{updated_about_me} -> updated bio")
    
    updated_biography = input(f"Change {hero_to_update}'s biography to: ")
    if updated_biography == "NO CHANGE":
        #do nothing??
        print("do nothing; this text is here so Python doesn't get mad")
    else:
        query = (""" 
                    UPDATE heroes
                    SET biography = %s
                    WHERE name = hero_to_update
                """)
        execute_query(query,(updated_biography,))


#✅DELETE==========================================================================
def delete_hero(hero_to_delete=None):
    hero_to_delete = input('Type the name of the hero whose profile you wish to DELETE: ')
    pollice_verso = input(f'Are you sure you want to delete {hero_to_delete}? Enter [YES] or [NO]: ')
    
    if pollice_verso == "YES" or "yes" and len(pollice_verso)==3:
        print(f"{hero_to_delete} has been deleted")
        query = ("""
                    DELETE FROM heroes WHERE name = %s
                """)
        execute_query(query,(hero_to_delete,))
        menu()

    elif pollice_verso == "NO" or "no" and len(pollice_verso)==2:
        cold_feet = input("Would you like to delete a different hero [DEL], or return to the menu [M]?")
        if cold_feet == "DEL":
            delete(hero_to_delete)
        elif cold_feet == "M":
            menu()


#LOGIN PAGE============================================================================

user = input("Welcome to SuperBase. Log in as: ")
password = input("Input password: ")
#make it more fun 
    #add a password? wrong pass = booted
    #SuperBase is a secret government database??
    #Barbara Gordon/Oracle's database (input "BarbieG", get welcomed as "oracle")
    #villain's record of adversaries??
if user == "BarbieG" and password == "KYSS23":
    clear()
    print("Welcome back, Oracle.")
    menu()
else:
    print(f"Hello, {user}. You're not supposed to be here." + '\n' +
                "SECURITY PROTOCOLS INITIATED" + '\n' +
                f"TARGET INTRUDER: {user}")
    sleep(3)
    clear()
