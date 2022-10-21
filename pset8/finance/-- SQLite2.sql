-- SQLite
CREATE TABLE shares2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    symbol CHAR(8) NOT NULL UNIQUE
);

INSERT INTO shares2 SELECT * FROM shares;

DROP TABLE shares;

ALTER TABLE shares2 RENAME TO shares;

--
DELETE FROM orders WHERE id > 0;

--
SELECT id FROM shares WHERE symbol = 'IBM';