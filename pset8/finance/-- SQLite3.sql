-- SQLite
SELECT
    shares.symbol AS Symbol,
    shares.name AS Name,
    SUM(orders.shares) AS Shares,
    orders.by_price AS Price
FROM orders
INNER JOIN shares ON shares.id = orders.share_id
WHERE user_id = 1
GROUP BY Symbol;

SELECT symbol FROM shares;

SELECT cash FROM users;

SELECT shares.symbol
FROM orders
INNER JOIN shares ON shares.id = orders.share_id
WHERE user_id = 1
GROUP BY Symbol;

SELECT shares.symbol AS symbol
FROM orders
INNER JOIN shares ON shares.id = orders.share_id
WHERE user_id = 1
GROUP BY symbol;

SELECT SUM(orders.shares) AS Shares
FROM orders
INNER JOIN shares ON shares.id=orders.share_id 
WHERE user_id = 1 AND symbol = 'IBM';