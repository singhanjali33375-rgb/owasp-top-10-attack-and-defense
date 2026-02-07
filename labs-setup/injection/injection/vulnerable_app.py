from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    user = request.args.get("user")
    query = f"SELECT * FROM users WHERE username = '{user}'"
    return query

app.run(debug=True)
