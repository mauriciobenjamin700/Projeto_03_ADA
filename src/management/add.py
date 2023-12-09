def add_customers(conn,first_name,last_name,phone,email,street,city,state,zip_code):
        
    cursor = conn.cursor()
    query = "INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)"
    values = (first_name, last_name, phone,email,street,city,state,zip_code) 
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

def add_stores(conn,store_name, phone, email, street, city, state, zip_code):
    
    cursor = conn.cursor()
    query = "INSERT INTO stores (store_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s,%s, %s, %s,%s)" 
    values = (store_name, phone, email, street, city, state, zip_code)  
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_staffs(conn,store_id, email, active, phone, first_name, last_name):
    
    cursor = conn.cursor()
    query = "INSERT INTO staffs (store_id, email, active, phone, first_name, last_name) VALUES (%s, %s, %s,%s, %s, %s)" 
    values = (store_id, email, active, phone, first_name, last_name)  
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_csv_orders(conn,customer_id, staff_id, order_status, order_date, required_date, shipped_date):
    
    cursor = conn.cursor()
    query = "INSERT INTO orders (customer_id, staff_id, order_status, order_date, required_date, shipped_date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (customer_id, staff_id, order_status, order_date, required_date, shipped_date)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_brands(conn,brand_name):
    
    cursor = conn.cursor()
    query = "INSERT INTO brands (brand_name) VALUES (%s)"
    values = (brand_name,) #virgula garante que isso é uma tupla e não uma string
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

def add_categories(conn,category_name):
    
    cursor = conn.cursor()
    query = "INSERT INTO categories (category_name) VALUES (%s)"
    values = (category_name,) #virgula garante que isso é uma tupla e não uma string
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_products(conn,brand_id,category_id,product_name,model_year,list_price):
    
    cursor = conn.cursor()
    query = "INSERT INTO products (brand_id,category_id,product_name,model_year,list_price) VALUES (%s,%s,%s,%s,%s)"
    values = (brand_id,category_id,product_name,model_year,list_price) 
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_order_items(conn,order_id,product_id,quantity,list_price,discount):
    
    cursor = conn.cursor()
    query = "INSERT INTO order_items (order_id,product_id,quantity,list_price,discount) VALUES (%s,%s,%s,%s,%s)"
    values = (order_id,product_id,quantity,list_price,discount) 
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
def add_stocks(conn,store_id,product_id,quantity):
    
    cursor = conn.cursor()
    query = "INSERT INTO stocks (store_id,product_id,quantity) VALUES (%s,%s,%s)"
    values = (store_id,product_id,quantity) 
    cursor.execute(query, values)
    conn.commit()
    cursor.close()