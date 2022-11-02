from database.connection import create_connection

def test_connnection_successful():
    assert create_connection('postgres', 'postgres', 'postgres') == "Connection sucessful"

def test_connection_failed():
    assert creat_connection('postgres', 'postgres', 'fsgrsfdjnj') == "Connection failed"