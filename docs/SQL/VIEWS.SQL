CREATE VIEW maiores_compras as
SELECT order_id, SUM(list_price * quantity) as valor_total
FROM order_items
GROUP BY order_id
ORDER BY valor_total DESC


CREATE VIEW produtos_caros_top20 AS
SELECT product_name, list_price
FROM products
ORDER BY list_price DESC
LIMIT 20;


CREATE VIEW clientes_por_cidade AS
SELECT city, COUNT(customer_id) AS quantidade_clientes
FROM customers
GROUP BY city
ORDER BY quantidade_clientes DESC;


CREATE VIEW produtos_baratos_top20 AS
SELECT product_name, list_price
FROM products
ORDER BY list_price ASC
LIMIT 20;

CREATE VIEW marca_mais_vendida AS
SELECT b.brand_id, b.brand_name, COUNT(oi.quantity) AS total_sold
FROM brands b
JOIN products p ON b.brand_id = p.brand_id
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY b.brand_id, b.brand_name
ORDER BY total_sold DESC
LIMIT 1;

CREATE MATERIALIZED VIEW materialized_clientes_por_cidade AS
select * from clientes_por_cidade;

CREATE VIEW produtos_mais_vendidos AS
SELECT sum(order_items.quantity) AS qtd_total,
order_items.product_id,
products.product_name
FROM order_items
JOIN products ON order_items.product_id = products.product_id
GROUP BY order_items.product_id, products.product_name
ORDER BY (sum(order_items.quantity)) DESC;
