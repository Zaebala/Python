from flask import Flask, render_template, request, g
import sqlite3
from post import FDataBase

app = Flask(__name__)


def connect_db():
    con = sqlite3.connect("C:/Users/adski/Desktop/Projects/TestServer/Guess.db")
    return con


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/search", methods=["POST", "GET"])
def search():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        name = request.form['name']
        size = request.form['size']
        gender = request.form['gender']
        return render_template('search.html', title="По вашему запросу найдено", post=dbase.get_staff(name, size, gender))


@app.route("/page_male")
def male():
    return render_template('page_male.html')


@app.route("/page_female")
def female():
    return render_template('page_female.html')


@app.route("/", methods=["GET", "POST"])
def gender():
    if request.method == "POST":
        if request.form['Gender'] == "GuessMale":
            return render_template('page_male.html')
        elif request.form['Gender'] == "GuessFemale":
            return render_template('page_female.html')
    return render_template('menu.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
