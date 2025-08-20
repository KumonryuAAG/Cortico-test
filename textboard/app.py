from flask import Flask, request, redirect, url_for, render_template
import sqlite3
import os

app = Flask(__name__)

DB_FILE = os.path.join(os.getcwd(), "data", "messages.db")
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

# Create table with name + content
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        msg = request.form.get("message")
        if name and msg:
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO messages (name, content) VALUES (?, ?)", (name, msg))
            conn.commit()
            conn.close()
        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name, content FROM messages ORDER BY id DESC")
    messages = c.fetchall()
    conn.close()

    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
