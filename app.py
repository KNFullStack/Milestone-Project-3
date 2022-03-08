import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np


if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=1)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/dashboard")
def dashboard():
    if not "user" in session:
        flash("Please log in.")
        return redirect(url_for("login"))


    user = session["user"].lower()
    income = mongo.db.income.find({"created_by": user})
    outgoings = mongo.db.outgoings.find({"created_by": user})

    # continue HERE
    # x = [1,2,3,4,5]
    # y = ["bill 1", "bill 2", "bill 3", "bill 4", "bill 5"]
    # pie = plt.pie(x, labels = y, autopct = "%2.1f%%")
    
    return render_template("dashboard.html", income=income, outgoings=outgoings, pie=pie)


@app.route("/login", methods=["GET","POST"])
def login():
    if "user" in session:
        flash("You are already logged in.")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session.permanent = True
                flash("Welcome back, {}.".format(request.form.get("username")))
                return redirect(url_for("dashboard", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password.")
                return redirect(url_for("login"))
    
        else:
            flash("Incorrect Username and/or Password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if "user" in session:
        flash("You must log out first.")
        return redirect(url_for("dashboard"))
    
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()

        flash("Successfully registered!")
        return redirect(url_for("dashboard", username=session["user"]))
    return render_template("register.html")


@app.route("/logout")
def logout():
    if "user" in session:
        flash("You have been logged out.")
        session.pop("user")
        return redirect(url_for('login'))
    else:
        flash("You are not logged in.")
        return redirect(url_for('login'))


@app.route("/add_income", methods=["GET","POST"])
def add_income():
    if not "user" in session:
        flash("Please log in.")
        return redirect(url_for("login"))
    if request.method == "POST":
        user = session["user"].lower()    
        income = {
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }
        mongo.db.income.insert_one(income)
        flash("Income added succesfully")
        return redirect(url_for("dashboard"))

    return render_template("income.html")


@app.route("/add_outgoing", methods=["GET","POST"])
def add_outgoing():
    if not "user" in session:
        flash("Please log in.")
        return redirect(url_for("login"))
    if request.method == "POST":
        user = session["user"].lower()    
        outgoing = {
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }
        mongo.db.outgoings.insert_one(outgoing)
        flash("Outgoing added succesfully")
        return redirect(url_for("dashboard"))
    return render_template("outgoing.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)