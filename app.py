import os
from datetime import timedelta
from io import BytesIO
import base64
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt
from flask_humanize import Humanize


if os.path.exists("env.py"):
    import env


app = Flask(__name__)
humanize = Humanize(app)
app.permanent_session_lifetime = timedelta(days=1)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Homepage route


@app.route("/")
def home():
    """ homepage route that renders the base.html document """
    return render_template("base.html")


# Dashboard route
@app.route("/dashboard")
def dashboard():
    """ dashboard route that renders a dashboard with
    pie charts and tables with values that have been entered """
    if "user" not in session:
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
    plt.pie(pie_chart_values_income, autopct="%2.0f%%", pctdistance=0.9)
    plt.tight_layout()
    plt.legend(title="Income:", bbox_to_anchor=(0.9, 1), loc="upper left",
               labels=pie_chart_label_income)
    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)
    graph = base64.b64encode(img.getvalue()).decode("utf8")

    # outgoings chart
    piechart_values_outgoings = []
    pie_chart_label_outgoings = []
    outgoings_list = list(mongo.db.outgoings.find({"created_by": user}))
    for item in outgoings_list:
        pie_chart_label_outgoings.append(item["name"].capitalize())
        piechart_values_outgoings.append(int(item["value"]))
    total_outgoings = sum(piechart_values_outgoings)
    img2 = BytesIO()
    plt.pie(piechart_values_outgoings, autopct="%2.0f%%", pctdistance=0.9)
    plt.tight_layout()
    plt.legend(title="Outgoings:", bbox_to_anchor=(0.9, 1), loc="upper left",
               labels=pie_chart_label_outgoings)
    plt.savefig(img2, format="png")
    plt.close()
    img.seek(0)
    graph2 = base64.b64encode(img2.getvalue()).decode("utf8")

    net = total_income - total_outgoings

    return render_template("dashboard.html", income=income,
                           outgoings=outgoings, graph=graph, graph2=graph2,
                           pie_chart_label_outgoings=pie_chart_label_outgoings,
                           piechart_values_outgoings=piechart_values_outgoings,
                           outgoings_list=outgoings_list,
                           total_outgoings=total_outgoings,
                           total_income=total_income, net=net)


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    """ login functionality """
    if "user" in session:
        flash("You are already logged in.")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.
                                                get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.
                                   get("password")):
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

# Register route


@app.route("/register", methods=["GET", "POST"])
def register():
    """ register functionality """
    if "user" in session:
        flash("You must log out first.")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.
                                                get("username").lower()})

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


# Logout route
@app.route("/logout")
def logout():
    """ logout functionality """
    if "user" in session:
        flash("You have been logged out.")
        session.pop("user")
        return redirect(url_for('login'))
    else:
        flash("You are not logged in.")
        return redirect(url_for('login'))


# Add income route
@app.route("/add_income", methods=["GET", "POST"])
def add_income():
    """ functionality to add an income """
    if "user" not in session:
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


# Add outgoing route
@app.route("/add_outgoing", methods=["GET", "POST"])
def add_outgoing():
    """ functionality to add an outgoing """
    if "user" not in session:
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


# Edit income route
@app.route("/edit_income/<item_id>", methods=["GET", "POST"])
def edit_income(item_id):
    """ functionality to edit an income """
    if request.method == "POST":
        user = session["user"].lower()
        old_name = mongo.db.income.find_one({"_id": ObjectId(item_id)})["name"]
        old_value = mongo.db.income.find_one(
                    {"_id": ObjectId(item_id)})["value"]
        income = {"$set": {
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }}

        name_comparison_i = income["$set"]["name"]
        value_comparison_i = income["$set"]["value"]

        if old_name == name_comparison_i and old_value == value_comparison_i:
            flash("There is no change to make.")
            return redirect(url_for("dashboard"))

        mongo.db.income.update_one({"_id": ObjectId(item_id)}, income)
        flash("Income changed.")

    item = mongo.db.income.find_one({"_id": ObjectId(item_id)})
    return render_template("edit_income.html", item=item)


# Add outgoing route
@app.route("/edit_outgoing/<item_id>", methods=["GET", "POST"])
def edit_outgoing(item_id):
    """ functionality to edit an outgoing """
    if request.method == "POST":
        user = session["user"].lower()
        old_name = mongo.db.outgoings.find_one(
                   {"_id": ObjectId(item_id)})["name"]
        old_value = mongo.db.outgoings.find_one(
                   {"_id": ObjectId(item_id)})["value"]
        outgoing = {"$set": {
            "name": request.form.get("name").lower(),
            "value": request.form.get("value").lower(),
            "created_by": user
        }}

        name_comparison_o = outgoing["$set"]["name"]
        value_comparison_o = outgoing["$set"]["value"]

        if old_name == name_comparison_o and old_value == value_comparison_o:
            flash("There is no change to make.")
            return redirect(url_for("dashboard"))

        mongo.db.outgoings.update_one({"_id": ObjectId(item_id)}, outgoing)
        flash("Outgoing changed.")

    item = mongo.db.outgoings.find_one({"_id": ObjectId(item_id)})
    return render_template("edit_outgoing.html", item=item)


# Delete income route
@app.route("/delete_income/<item_id>")
def delete_income(item_id):
    """ functionality to delete an income """
    mongo.db.income.delete_one({"_id": ObjectId(item_id)})
    flash("Income Removed")
    return redirect(url_for("dashboard"))


# Delete outgoing route
@app.route("/delete_outgoing/<item_id>")
def delete_outgoing(item_id):
    """ functionality to delete an outgoing """
    mongo.db.outgoings.delete_one({"_id": ObjectId(item_id)})
    flash("Outgoing Removed")
    return redirect(url_for("dashboard"))


# 404 page created in case of errors - can return to homepage
@app.errorhandler(404)
def not_found(e):
    """ handles a 404 error where a specific 404.html document is displayed """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=False)
