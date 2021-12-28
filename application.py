import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///booklist.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        title=request.form.get("title")
        author=request.form.get("author")
        category=request.form.get("category")
        read=request.form.get("read")
        if not title:
            message="Missing title"
        elif not author:
            message="Missing author"
        elif not category:
            message="Missing category"
        elif not read:
            message="Missing read"
        else:
            db.execute("INSERT INTO booklist (title, author, category,read) VALUES(?,?,?,?)", title, author, category, read)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        booklist=db.execute("SELECT * FROM booklist")

        return render_template("index.html", booklist=booklist)