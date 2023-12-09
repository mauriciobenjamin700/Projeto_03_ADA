import pandas as pd


def add_csv_customers(conn,csv_file):
    
    df = pd.read_csv(csv_file)
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        query = "INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)"  # ajuste para suas colunas
        values = (row['first_name'], row['last_name'], row['phone'],row['email'],row['street'],row['city'],row['state'],row['zip_code'],)  # ajuste para seus nomes de colunas
        cursor.execute(query, values)

    conn.commit()
    cursor.close()

def add_csv_stores(conn,csv_file):
    
    df = pd.read_csv(csv_file)
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        query = "INSERT INTO stores (store_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s)" 
        values = (row['store_name'], row['phone'],row['email'],row['street'],row['city'],row['state'],row['zip_code'],)  
        cursor.execute(query, values)
        
        
    conn.commit()
    cursor.close()
    
def add_csv_staffs(conn,csv_file):
    
    df = pd.read_csv(csv_file)
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        query = "INSERT INTO staffs (store_id, email, active, phone, first_name, last_name) VALUES (%s, %s, %s,%s, %s, %s)" 
        values = (row['store_id'],row['email'],row['active'],row['phone'],row['first_name'],row['last_name'],)  
        cursor.execute(query, values)
        
        
        
    conn.commit()
    cursor.close()
    
    
def add_csv_orders(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
        
        if pd.isnull(row['shipped_date']):
            shipped_date = None
        else:
            shipped_date = row['shipped_date']

        query = "INSERT INTO orders (customer_id, staff_id, order_status, order_date, required_date, shipped_date) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (row['customer_id'], row['staff_id'], row['order_status'], row['order_date'], row['required_date'], shipped_date)
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()
    

def add_csv_brands(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
        
        
        query = "INSERT INTO brands (brand_name) VALUES (%s)"
        values = (row['brand_name'],) #virgula garante que isso é uma tupla e não uma string
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()

def add_csv_categories(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
                
        query = "INSERT INTO categories (category_name) VALUES (%s)"
        values = (row['category_name'],) #virgula garante que isso é uma tupla e não uma string
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()
    
def add_csv_products(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
                
        query = "INSERT INTO products (brand_id,category_id,product_name,model_year,list_price) VALUES (%s,%s,%s,%s,%s)"
        values = (row['brand_id'],row['category_id'],row['product_name'],row['model_year'],row['list_price']) 
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()
    
def add_csv_order_items(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
                
        query = "INSERT INTO order_items (order_id,product_id,quantity,list_price,discount) VALUES (%s,%s,%s,%s,%s)"
        values = (row['order_id'],row['product_id'],row['quantity'],row['list_price'],row['discount']) 
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()
    
def add_csv_stocks(conn,csv_file):
    
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
                
        query = "INSERT INTO stocks (store_id,product_id,quantity) VALUES (%s,%s,%s)"
        values = (int(row['store_id']),int(row['product_id']),int(row['quantity'])) 
        cursor.execute(query, values)
        
    conn.commit()
    cursor.close()