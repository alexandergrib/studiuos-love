import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask import render_template

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html", index_page=True)


@app.route("/love_facts")
def love_facts():
    return render_template("love_facts.html")


@app.route("/topten")
def topten():
    data1 = []
    with open("data/RomanticMovies.json", "r") as json_data1:
        data1 = json.load(json_data1)

    data2 = []
    with open("data/RomanticPlaces.json", "r") as json_data2:
        data2 = json.load(json_data2)

    data3 = []
    with open("data/RomanticQuotes.json", "r") as json_data3:
        data3 = json.load(json_data3)

    return render_template("topten.html", movies=data1, places=data2, quotes=data3)


@app.route("/poetry", methods=['GET', 'POST'])
def poetry():
    poem_list = list(mongo.db.poetry.find())
    if request.method == "POST":
        submit = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "text": request.form.get("text"),
            "copyright": request.form.get("copyright")
        }
        flash_text = "{} Successfully Created".format(
            submit["title"])
        flash(flash_text)
        mongo.db.poetry.insert_one(submit)
        flash('flash_text')
        return redirect(url_for('poetry'))
    return render_template("poems.html", poem_list=poem_list)


@app.route("/gifts")
def gift_ideas():
    return render_template("gift_ideas.html")


# User section Login Logout Profile------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("index"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
