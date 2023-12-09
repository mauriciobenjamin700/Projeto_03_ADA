def select_all(conn,table):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table}"
    
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    cursor.close()
    
    return result

def select_where(conn,table,column,conteudo):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table} WHERE {column} = {conteudo}"
    
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    cursor.close()
    
    return result