def update_rows(conn, table, set_values, condition):
    
    cursor = conn.cursor()
    query = f"UPDATE {table} SET {set_values} WHERE {condition}"
    cursor.execute(query)
    conn.commit()
    cursor.close()