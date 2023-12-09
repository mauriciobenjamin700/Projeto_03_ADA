def drop_scheme(conn):
    
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

    # Excluir todas as tabelas
    for table in tables:
        drop_query = f"DROP TABLE IF EXISTS {table[0]} CASCADE;"
        cursor.execute(drop_query)

    # Confirmar as alterações e fechar a conexão
    conn.commit()
    cursor.close()
    