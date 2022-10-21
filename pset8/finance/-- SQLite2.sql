-- SQLite
INSERT INTO shares2 SELECT * FROM shares;


ALTER TABLE shares2 RENAME TO shares;


DELETE FROM orders WHERE id > 0;


SELECT id FROM shares WHERE symbol = 'IBM';