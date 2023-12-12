CREATE VIEW maiores_compras as
SELECT order_id, SUM(list_price * quantity) as valor_total
FROM order_items
GROUP BY order_id
ORDER BY valor_total DESC

