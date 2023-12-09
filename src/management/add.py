import pandas as pd

def add_customers(cursor):
    pass

def add_csv_customers(cursor,csv_file):
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        query = "INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)"  # ajuste para suas colunas
        values = (row['first_name'], row['last_name'], row['phone'],row['email'],row['street'],row['city'],row['state'],row['zip_code'],)  # ajuste para seus nomes de colunas
        cursor.execute(query, values)


def add_csv_stores(cursor,csv_file):
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        query = "INSERT INTO stores (store_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s)"  # ajuste para suas colunas
        values = (row['store_name'], row['phone'],row['email'],row['street'],row['city'],row['state'],row['zip_code'],)  # ajuste para seus nomes de colunas
        cursor.execute(query, values)
        
def add_csv_staffs(cursor,csv_file):
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        query = "INSERT INTO staffs (store_id, email, active, phone, first_name, last_name) VALUES (%s, %s, %s,%s, %s, %s)"  # ajuste para suas colunas
        values = (row['store_id'],row['email'],row['active'],row['phone'],row['first_name'],row['last_name'],)  # ajuste para seus nomes de colunas
        cursor.execute(query, values)
        
def add_csv_orders(cursor,csv_file):
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        query = "INSERT INTO staffs (store_id, customer_id, staff_id, order_status, order_date, required_data) VALUES (%s, %s, %s,%s, %s, %s)"  # ajuste para suas colunas
        values = (row['store_id'],row['email'],row['active'],row['phone'],row['first_name'],row['last_name'],)  # ajuste para seus nomes de colunas
        cursor.execute(query, values)