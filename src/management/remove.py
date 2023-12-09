def delete_rows(conn,table,condition):
    cursor = conn.cursor()
    query = f"DELETE FROM {table} WHERE {condition}"
    cursor.execute(query)
    conn.commit()
    cursor.close()