from configparser import ConfigParser
from psycopg2 import connect, OperationalError


# kod odp za łączenie się z bazą danych
def connect_to_db():
    try:
        config = ConfigParser()
        config.read('etc/config.ini')
        cnx = connect(
            user=config.get('db', 'username'),
            password=config.get('db', 'password'),
            host=config.get('db', 'host'),
            database=config.get('db', 'database')
        )
        cnx.autocommit = True
        return cnx
    except OperationalError as e:
        print(e)
    else:
        cnx.close()