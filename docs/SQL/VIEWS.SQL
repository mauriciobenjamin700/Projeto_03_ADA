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
SELECT b.brand_id, b.brand_name, SUM(oi.quantity) AS total_sold
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

create view categoria_mais_vendida as
select categories.category_name, sum(order_items.quantity) as total from categories
join products on categories.category_id = products.category_id
join order_items on products.product_id = order_items.product_id
group by categories.category_name
order by total desc;


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


CREATE VIEW ticket_medio AS
SELECT
    COUNT(DISTINCT order_items.order_id) AS pedidos,
	(SUM(order_items.list_price * order_items.quantity)/COUNT(DISTINCT order_items.order_id)) as ticket_medio
FROM
    order_items;

CREATE VIEW stock_total_por_item as
 SELECT products.product_name,
    stocks.product_id,
    sum(stocks.quantity) AS stock_total
   FROM stocks
     JOIN products ON stocks.product_id = products.product_id
  GROUP BY stocks.product_id, products.product_name
  ORDER BY stocks.product_id;

CREATE VIEW stock_total_por_loja as
 SELECT stocks.store_id,
    sum(stocks.quantity) AS stock_total
   FROM stocks
  GROUP BY stocks.store_id;