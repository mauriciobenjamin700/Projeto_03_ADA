def show_database(conn):
    query = "SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public';"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    cursor.close()
    return result


def show_atributes_table(conn,table_name):
    query = f"""
        SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = '{table_name}';
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    cursor.close()
    return result
