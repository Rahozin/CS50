-- Create tables
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    share_id INTEGER NOT NULL,
    shares INTEGER NOT NULL,
    by_price REAL NOT NULL,
    date_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE shares (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    symbol CHAR(8) NOT NULL UNIQUE
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    username VARCHAR(255) NOT NULL UNIQUE,
    hash TEXT VARCHAR(255) NOT NULL,
    cash REAL NOT NULL DEFAULT 10000.00
);


-- Delete tables(for clear all data)
DROP TABLE orders;


-- Delete specific rows from table
DELETE FROM orders
WHERE id < 10;


-- Change data in db
UPDATE users
SET cash = 7519.13
WHERE id = 1;


-- 
INSERT INTO shares2 SELECT * FROM shares;

ALTER TABLE shares2 RENAME TO shares;

SELECT id FROM shares WHERE symbol = 'IBM';

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
GROUP BY symbol;

SELECT SUM(orders.shares) AS Shares
FROM orders
INNER JOIN shares ON shares.id=orders.share_id 
WHERE user_id = 1 AND symbol = 'IBM';