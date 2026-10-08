import sqlite3

connection = sqlite3.connect(
    "database/game_tracker.db",
    check_same_thread=False
)
def add_game(name, release_date, developer, publisher, rating):
    cursor = connection.execute("""
        INSERT INTO games (name, release_date, developer, publisher, rating)
        VALUES (?, ?, ?, ?, ?)
    """, (name, release_date, developer, publisher, rating))

    connection.commit()

    return cursor.lastrowid       #concept:gives us the ID Sqlite assigned to newly insrted game so that we can distinguish


def add_platform(name):
    connection.execute("""
        INSERT INTO platforms (name)
        VALUES (?)
    """, (name,))

    connection.commit()


def add_game_platform(game_id, platform_id):
    connection.execute("""
        INSERT INTO game_platforms (game_id, platform_id)
        VALUES (?, ?)
    """, (game_id, platform_id))

    connection.commit()


def get_games():
    result = connection.execute("""
        SELECT * FROM games
    """).fetchall()

    return result

def get_game(game_id):
    result = connection.execute("""
        SELECT * FROM games
        WHERE id = ?
    """, (game_id,)).fetchone()

    return result

def update_game(game_id,rating):
    connection.execute("""
        UPDATE games
        SET rating = ?
        WHERE id = ?
    """,(rating,game_id))

    connection.commit()


def delete_game(game_id):
    connection.execute("""
        DELETE FROM games
        WHERE id = ?
    """, (game_id,))

    connection.commit()

def get_game_with_platform(game_id):
    result = connection.execute("""
        SELECT games.name, platforms.name
        FROM games
        JOIN game_platforms
            ON games.id = game_platforms.game_id
        JOIN platforms
            ON game_platforms.platform_id = platforms.id
        WHERE games.id = ?
    """, (game_id,)).fetchall()

    return result


def get_platforms():
    platforms = connection.execute("""
        SELECT name FROM platforms
    """).fetchall()

    return platforms()


def get_platform(id):
    result = connection.execute("""
        SELECT * FROM platforms
        WHERE id = ?
    """, (id,)).fetchone()

    return result

def del_platform(id):
    connection.execute("""
        DELETE FROM platforms
        WHERE id = ?
    """, (id,))

    connection.commit()


