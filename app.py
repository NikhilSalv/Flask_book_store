from flask import Flask, render_template, request, redirect
import sqlite3
from cs50 import SQL
import os


app = Flask(__name__)

db = SQL("sqlite:///Books.db")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addbook", methods= ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("Book")
        author = request.form.get("Author")
        if not name or not author:
            return redirect("/faliure")
        
        db.execute("INSERT INTO books (name, author) VALUES(?,?)", name, author)
        return redirect("/booklist")

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