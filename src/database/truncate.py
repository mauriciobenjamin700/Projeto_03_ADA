def truncate_scheme(conn):
    
    cursor = conn.cursor()
    
    # Consulta para obter todas as tabelas existentes
    query_get_tables = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """

    # Executar a consulta
    cursor.execute(query_get_tables)
    tables = cursor.fetchall()

    # Limpar dados de todas as tabelas usando TRUNCATE
    for table in tables:
        truncate_query = f"TRUNCATE TABLE {table[0]} RESTART IDENTITY CASCADE;"
        cursor.execute(truncate_query)


    conn.commit()
    cursor.close()
    