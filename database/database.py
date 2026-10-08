import sqlite3

connection = sqlite3.connect("game_tracker.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    release_date TEXT NOT NULL,
    developer TEXT NOT NULL,
    publisher TEXT,
    rating FLOAT
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS platforms (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS game_platforms (
    game_id INTEGER,
    platform_id INTEGER,
    PRIMARY KEY (game_id, platform_id),
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (platform_id) REFERENCES platforms(id)
)
""")

connection.commit()


