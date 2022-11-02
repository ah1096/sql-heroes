from database.connection import execute_query

def select_all():
    query = """
        SELECT * from TEST
    """

    execute_query(query)

"something %s".format('DROP * TABLES;')

def select_where_int(integer):
    integer = input('Which number should we look up? ')
    print(integer)
    print('hello')
    query = """
            SELECT * from test WHERE num = %s
        """

    params = (integer,)

    records = execute_query(query, params)
    print(records)

select_where_int(10)