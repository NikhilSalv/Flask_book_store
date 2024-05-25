from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import sqlite3
from cs50 import SQL
import os


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///Books.db")


@app.route("/", methods = ["POST", "GET"])
def index():

    return render_template("index.html", name = session.get("name"))

@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("Login.html")


@app.route("/addbook", methods= ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("Book")
        author = request.form.get("Author")
        if not name or not author:
            return redirect("/faliure")
        
        db.execute("INSERT INTO books (name, author) VALUES(?,?)", name, author)
        return redirect("/")

@app.route("/faliure")
def failure():
    return render_template("failure.html")

@app.route("/booklist")
def booklist():
    book_list = db.execute("SELECT * FROM books")
    return render_template("booklist.html", books = book_list)

@app.route("/delete/<int:book_id>", methods =["POST", "GET"] )
def deletebook(book_id):
    if request.method == "POST":
        # book_id = request.form.get("book_id")
        db.execute("DELETE FROM books WHERE book_id = ?" , book_id)
        return redirect("/booklist")

@app.route("/cart", methods=["GET", "POST"])
def addtocart():
    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        book_id = request.form.get("book_id")
        session["cart"].append(book_id)
        return redirect("/booklist")
    if request.method == "GET":
        if session["cart"]:
            placeholder = ", ".join("?" for _ in session["cart"])
            query = f"SELECT * FROM books WHERE book_id IN ({placeholder})"
            cart_list = db.execute(query, *session["cart"])
        else:
            cart_list = []
        return render_template("cart.html", cart_list=cart_list)


# @app.route("/showcart")
# def showcart():
#     cart_list = db.execute("SELECT * FROM books WHERE book_id IN (?)", session["cart"])
#     return render_template("cart.html", cart_list=cart_list)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# name = "Book1"
# author  = "Author1"

# db.execute("INSERT INTO books (name, author) VALUES(?,?)", name, author)
# db.execute("DELETE FROM books WHERE book_id = 1")



# cursor = connection.cursor()

# # Step 3: Execute a SQL command to create the table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS books (
#     book_id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     author TEXT NOT NULL
# )
# ''')

# # Step 4: Commit the changes
# connection.commit()


if __name__ == "__main__":
    app.run(debug=True)