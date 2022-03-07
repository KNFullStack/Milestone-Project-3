import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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

# tests = mongo.db.testing.find() - this is how we get our records from testing collection

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/dashboard")
def dashboard():
    income = mongo.db.income.find()
    outgoings = mongo.db.outgoings.find()
    return render_template("dashboard.html", income=income, outgoings=outgoings)


@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("register.html")


@app.route("/logout")
def logout():
    # do xyz
    # do flash
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)