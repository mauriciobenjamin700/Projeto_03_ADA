import psycopg2 as sql


def connect_db(database_name="second_db",user_name="postgres",user_password="14148099",user_host="localhost",user_port=1024):
    
    
    connection = sql.connect(
            dbname=database_name,
            user=user_name,
            password=user_password,
            host=user_host,
            port=user_port 
        )

    return connection


def bike_db():
    return connect_db(database_name='bmrlylsu',user_name='bmrlylsu',user_password='dEJ1yEK_MDfJqWO0UVVsbwxy6_7hcLd_',user_host='isabelle.db.elephantsql.com',user_port=5432)
    