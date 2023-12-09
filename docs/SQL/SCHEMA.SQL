/*
CREATE DATABASE IF NOT EXISTS bike_store;
*/

CREATE TABLE IF NOT EXISTS customers
(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100),
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(30)
);


CREATE TABLE IF NOT EXISTS stores
(
    store_id SERIAL PRIMARY KEY,
    store_name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS staffs
(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    active char(1),
    store_id SMALLINT ,
    

    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE IF NOT EXISTS orders 
(
    order_id SERIAL PRIMARY KEY,
    customer_id SMALLINT ,
    staff_id SMALLINT,
    order_status CHAR(1),
    order_date DATE,
    required_date DATE,
    shipped_date DATE,

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (staff_id) REFERENCES staffs(staff_id)
);


CREATE TABLE IF NOT EXISTS brands
(
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS categories
(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS products
(
    product_id SERIAL PRIMARY KEY,
    brand_id SMALLINT,
    category_id SMALLINT,
    product_name VARCHAR(100),
    model_year SMALLINT,
    list_price FLOAT(2),

    FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS order_items 
(
    order_id SMALLINT,
    product_id SMALLINT,
    quantity SMALLINT,
    list_price FLOAT(2),
    discount FLOAT(2),

    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS stocks
(
    store_id SMALLINT,
    product_id SMALLINT,
    quantity SMALLINT,

    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

