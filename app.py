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
from io import BytesIO
import base64

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

    # income chart
    pie_chart_values_income = []
    pie_chart_label_income = []
    income_list = list(mongo.db.income.find({"created_by": user}))
    for item in income_list:
        pie_chart_label_income.append(item["name"].capitalize())
        pie_chart_values_income.append(int(item["value"]))
    total_income = sum(pie_chart_values_income)
    img = BytesIO()
    plt.pie(pie_chart_values_income, autopct = "%2.0f%%", pctdistance=0.9)
    plt.tight_layout()
    plt.legend(title = "Income:", bbox_to_anchor=(0.9,1), loc="upper left", labels = pie_chart_label_income)
    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)
    graph = base64.b64encode(img.getvalue()).decode("utf8")

    # outgoings chart
    pie_chart_values_outgoings = []
    pie_chart_label_outgoings = []
    outgoings_list = list(mongo.db.outgoings.find({"created_by": user}))
    for item in outgoings_list:
        pie_chart_label_outgoings.append(item["name"].capitalize())
        pie_chart_values_outgoings.append(int(item["value"]))
    total_outgoings = sum(pie_chart_values_outgoings)
    img2 = BytesIO()
    plt.pie(pie_chart_values_outgoings, autopct = "%2.0f%%", pctdistance=0.9)
    plt.tight_layout()
    plt.legend(title = "Outgoings:", bbox_to_anchor=(0.9,1), loc="upper left", labels = pie_chart_label_outgoings)
    plt.savefig(img2, format="png")
    plt.close()
    img.seek(0)
    graph2 = base64.b64encode(img2.getvalue()).decode("utf8")

    return render_template("dashboard.html", income=income, outgoings=outgoings, graph=graph, graph2=graph2,
    pie_chart_label_outgoings=pie_chart_label_outgoings, pie_chart_values_outgoings=pie_chart_values_outgoings,
    outgoings_list=outgoings_list, total_outgoings=total_outgoings, total_income=total_income)


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


@app.route("/edit_income/<item_id>", methods=["GET","POST"])
def edit_income(item_id):

    if request.method == "POST":
        user = session["user"].lower()
        old_name = mongo.db.income.find_one({"_id": ObjectId(item_id)})["name"]
        old_value = mongo.db.income.find_one({"_id": ObjectId(item_id)})["value"]
        income = { "$set" :{
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }}
        
        if old_name == income["$set"]["name"] and old_value == income["$set"]["value"]:
            flash("There is no change to make.")
            return redirect(url_for("dashboard"))

        mongo.db.income.update_one({"_id": ObjectId(item_id)}, income)
        flash("Income changed.")

    item = mongo.db.income.find_one({"_id": ObjectId(item_id)})
    return render_template("edit_income.html", item=item)


@app.route("/edit_outgoing/<item_id>", methods=["GET","POST"])
def edit_outgoing(item_id):

    if request.method == "POST":
        user = session["user"].lower()
        old_name = mongo.db.outgoings.find_one({"_id": ObjectId(item_id)})["name"]
        old_value = mongo.db.outgoings.find_one({"_id": ObjectId(item_id)})["value"]
        outgoing = { "$set" :{
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }}

        if old_name == outgoing["$set"]["name"] and old_value == outgoing["$set"]["value"]:
            flash("There is no change to make.")
            return redirect(url_for("dashboard"))

        mongo.db.outgoings.update_one({"_id": ObjectId(item_id)}, outgoing)
        flash("Outgoing changed.")

    item = mongo.db.outgoings.find_one({"_id": ObjectId(item_id)})
    return render_template("edit_outgoing.html", item=item)


@app.route("/delete_income/<item_id>")
def delete_income(item_id):
    mongo.db.income.delete_one({"_id": ObjectId(item_id)})
    flash("Income Removed")
    return redirect(url_for("dashboard"))


@app.route("/delete_outgoing/<item_id>")
def delete_outgoing(item_id):
    mongo.db.outgoings.delete_one({"_id": ObjectId(item_id)})
    flash("Outgoing Removed")
    return redirect(url_for("dashboard"))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)