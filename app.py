from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("products.db")
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()
    return render_template("index.html", tables=df.to_html(classes='data'))

@app.route("/search")
def search():
    keyword = request.args.get("q", "")
    conn = sqlite3.connect("products.db")
    df = pd.read_sql("SELECT * FROM products WHERE Title LIKE ?", conn, params=('%'+keyword+'%',))
    conn.close()
    return render_template("index.html", tables=df.to_html(classes='data'))

if __name__ == "__main__":
    app.run(debug=True)
