DROP TABLE IF EXISTS post;

CREATE TABLE post(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author TEXT NOT NULL,
    message TEXT NOT NULL
);