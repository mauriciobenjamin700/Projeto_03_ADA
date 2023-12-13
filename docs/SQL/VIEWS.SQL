CREATE VIEW maiores_compras as
SELECT order_id, SUM(list_price * quantity) as valor_total
FROM order_items
GROUP BY order_id
ORDER BY valor_total DESC


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


CREATE VIEW loja_maior_renda AS
SELECT
    stores.store_id, 
    COUNT(DISTINCT orders.order_id) AS pedidos,
	SUM(order_items.list_price * order_items.quantity) as valor_total
FROM
    order_items
INNER JOIN
	orders ON order_items.order_id = orders.order_id
INNER JOIN
    staffs ON orders.staff_id = staffs.staff_id
INNER JOIN
    stores ON staffs.store_id = stores.store_id
GROUP BY
    stores.store_id
ORDER BY valor_total DESC