def create_scheme(conn,sql_filename):
    
    cursor = conn.cursor()

    sql_file = open(sql_filename, 'r')
    sql_script = sql_file.read()
    sql_file.close()

    cursor.execute(sql_script)
    
    conn.commit()
    cursor.close()
    
