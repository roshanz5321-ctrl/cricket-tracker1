import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

print("=== TOTAL PLAYERS ===")
cursor.execute("SELECT COUNT(*) FROM players")
print(f"Total: {cursor.fetchone()[0]}")

print("\n=== BY FORMAT ===")
cursor.execute("SELECT format, COUNT(*) FROM players GROUP BY format")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} players")

print("\n=== BY TEAM ===")
cursor.execute("SELECT team, COUNT(*) FROM players GROUP BY team ORDER BY team")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} players")

print("\n=== SAMPLE ODI PLAYERS ===")
cursor.execute("SELECT name, team, runs, wickets FROM players WHERE format='odi' LIMIT 10")
for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]}): {row[2]} runs, {row[3]} wickets")

conn.close()