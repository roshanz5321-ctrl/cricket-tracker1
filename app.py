from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/odi")
def odi_page():
    return render_template("odi.html")

@app.route("/t20")
def t20_page():
    return render_template("t20.html")

@app.route("/test")
def test_page():
    return render_template("test.html")

@app.route("/api/players/<format_name>")
def get_players(format_name):
    import sqlite3
    conn = sqlite3.connect("players.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE format = ?", (format_name,))
    rows = cursor.fetchall()
    conn.close()
    players = [dict(row) for row in rows]
    return jsonify(players)

@app.route("/api/players", methods=["POST"])
def add_player():
    import sqlite3
    data = request.get_json()

    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO players (name, team, format, hundreds, fifties, runs, wickets) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (data["name"], data["team"], data["format"], data["hundreds"], data["fifties"], data["runs"], data["wickets"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Player added successfully"})

if __name__ == "__main__":
   # ✅ Route ko IF block ke BAHAR rakho
 @app.route("/api/players/<format_name>/<player_name>", methods=["DELETE"])
 def delete_player(format_name, player_name):
    import sqlite3
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE format = ? AND name = ?", (format_name, player_name))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted > 0:
        return jsonify({"message": "Player deleted successfully"}), 200
    else:
        return jsonify({"message": "Player not found"}), 404


# ✅ Sirf app.run ko andar rakho
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    app.run(debug=True,host="0.0.0.0")