from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


# ==================== PAGES ====================

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

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/records")
def records_page():
    return render_template("records.html")

@app.route("/teams")
def teams_page():
    return render_template("teams.html")


# ==================== API ====================

@app.route("/api/players/<format_name>")
def get_players(format_name):
    conn = sqlite3.connect("players.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    # FIX: Case insensitive match
    cursor.execute("SELECT * FROM players WHERE LOWER(format) = LOWER(?)", (format_name,))
    rows = cursor.fetchall()
    conn.close()
    players = [dict(row) for row in rows]
    return jsonify(players)


@app.route("/api/players", methods=["POST"])
def add_player():
    data = request.get_json()

    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    # FIX: Format hamesha lowercase store karo
    cursor.execute(
        "INSERT INTO players (name, team, format, hundreds, fifties, runs, wickets) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (data["name"], data["team"], data["format"].lower(), data["hundreds"], data["fifties"], data["runs"], data["wickets"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Player added successfully"})


@app.route("/api/players/<format_name>/<player_name>", methods=["DELETE"])
def delete_player(format_name, player_name):
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    # FIX: Case insensitive delete
    cursor.execute("DELETE FROM players WHERE LOWER(format) = LOWER(?) AND name = ?", (format_name, player_name))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted > 0:
        return jsonify({"message": "Player deleted successfully"}), 200
    else:
        return jsonify({"message": "Player not found"}), 404


@app.route("/api/records")
def get_records():
    conn = sqlite3.connect("players.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Top Scorer
    cursor.execute("SELECT name, team, format, runs FROM players ORDER BY runs DESC LIMIT 1")
    row = cursor.fetchone()
    top_scorer = dict(row) if row else {"name": "N/A", "team": "N/A", "format": "N/A", "runs": 0}

    # Top Wicket Taker
    cursor.execute("SELECT name, team, format, wickets FROM players ORDER BY wickets DESC LIMIT 1")
    row = cursor.fetchone()
    top_wicket_taker = dict(row) if row else {"name": "N/A", "team": "N/A", "format": "N/A", "wickets": 0}

    # Most Centuries
    cursor.execute("SELECT name, team, format, hundreds FROM players ORDER BY hundreds DESC LIMIT 1")
    row = cursor.fetchone()
    top_centuries = dict(row) if row else {"name": "N/A", "team": "N/A", "format": "N/A", "hundreds": 0}

    conn.close()
    return jsonify({
        "top_scorer": top_scorer,
        "top_wicket_taker": top_wicket_taker,
        "top_centuries": top_centuries
    })


@app.route("/api/teams")
def get_teams():
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT team FROM players ORDER BY team")
    teams = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(teams)


# ==================== RUN ====================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")