from src.database.conection import connect_db
from src.database.create import create_scheme
from src.database.drop import drop_scheme
from src.database.truncate import truncate_scheme
from management.add_csv import *

# se seu SO é linux, use '/' como separador, caso seja windows use '\\'
PATH = 'docs/csv/'

def sistem():
    conn = connect_db(database_name='bmrlylsu',user_name='bmrlylsu',user_password='dEJ1yEK_MDfJqWO0UVVsbwxy6_7hcLd_',user_host='isabelle.db.elephantsql.com',user_port=5432)
        
    print("Conectei")
    truncate_scheme(conn)
    drop_scheme(conn)
    create_scheme(conn,'docs/SQL/SCHEMA.SQL')
    
    
    add_csv_customers(conn,'docs/csv/customers.csv')
    add_csv_stores(conn,PATH+'stores.csv')
    add_csv_staffs(conn,PATH+'staffs.csv')
    add_csv_orders(conn,PATH+'orders.csv')
    add_csv_brands(conn,PATH+'brands.csv')
    add_csv_categories(conn,PATH+'categories.csv')
    add_csv_products(conn,PATH+'products.csv')
    add_csv_order_items(conn,PATH+'order_items.csv')
    add_csv_stocks(conn,PATH+'stocks.csv')

    conn.close()
    print("terminei")


sistem()