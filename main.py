from src.database.conection import dataBase
from src.management.add import add_csv_customers,add_csv_stores,add_csv_staffs

conn = dataBase(database_name='bmrlylsu',user_name='bmrlylsu',user_password='dEJ1yEK_MDfJqWO0UVVsbwxy6_7hcLd_',user_host='isabelle.db.elephantsql.com',user_port=5432)

if conn != None:
    cursor = conn.cursor()

    print(conn)
    #add_csv_customers(cursor,'docs\\csv\\customers.csv')
    #add_csv_stores(cursor,'docs\\csv\\stores.csv')
    #add_csv_staffs(cursor,'docs\\csv\\staffs.csv')
    conn.commit()
    cursor.close()
    conn.close()
    print("terminei")
else:
    print("Falhei")
