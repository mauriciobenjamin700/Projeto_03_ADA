import psycopg2 as sql


def dataBase(database_name="second_db",user_name="postgres",user_password="14148099",user_host="localhost",user_port=1024):
    
    #
    connection = sql.connect(
        dbname=database_name,
        user=user_name,
        password=user_password,
        host=user_host,
        port=user_port  # Substitua pelo número correto da porta do seu banco de dados PostgreSQL
    )
    #except:
    #    connection = None

    return connection

# import psycopg2 as sql

# conec = sql.connect(host='localhost', port=1024, dbname='second_db', user='postgres', password='14148099', sslmode='prefer', connect_timeout=10)

# cursor = conec.cursor()

# cursor.execute('DROP TABLE IF EXISTS clientes')

# conec.commit()
# conec.close()