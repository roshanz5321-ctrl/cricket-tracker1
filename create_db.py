import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

# Purana table delete karo (fresh start ke liye)
cursor.execute("DROP TABLE IF EXISTS players")

# Naya table banao - format column ke saath
cursor.execute("""
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    format TEXT NOT NULL,
    hundreds INTEGER,
    fifties INTEGER,
    runs INTEGER,
    wickets INTEGER
)
""")

players = [
    # ODI data
    ("Virat Kohli", "India", "ODI", 54, 79, 14941, 4),
    ("Steve Smith", "Australia", "ODI", 12, 35, 5800, 8),
    ("Jasprit Bumrah", "India", "ODI", 0, 0, 200, 160),
    ("Joe Root", "England", "ODI", 20, 48, 7826, 30),
    ("Pat Cummins", "Australia", "ODI", 0, 0, 537, 143),

    # T20 data
    ("Virat Kohli", "India", "T20", 1, 38, 4188, 4),
    ("Suryakumar Yadav", "India", "T20", 4, 20, 2650, 0),
    ("Jasprit Bumrah", "India", "T20", 0, 0, 60, 89),
    ("David Warner", "Australia", "T20", 1, 24, 3277, 0),
    ("Rashid Khan", "Afghanistan", "T20", 0, 0, 500, 175),

    # Test data
    ("Joe Root", "England", "Test", 36, 66, 13542, 32),
    ("Virat Kohli", "India", "Test", 30, 32, 9230, 0),
    ("Pat Cummins", "Australia", "Test", 1, 15, 1897, 294),
    ("Steve Smith", "Australia", "Test", 33, 41, 10000, 20),
    ("Jasprit Bumrah", "India", "Test", 0, 0, 700, 210),
]

cursor.executemany(
    "INSERT INTO players (name, team, format, hundreds, fifties, runs, wickets) VALUES (?, ?, ?, ?, ?, ?, ?)",
    players
)

conn.commit()
conn.close()
print("Database recreated with format column and T20/Test data!")