-- SQLite
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    share_id INTEGER NOT NULL,
    shares INTEGER NOT NULL,
    by_price REAL NOT NULL,
    date_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
