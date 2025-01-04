from flask import render_template, request, redirect, url_for
from workouts import app, db
from workouts.models import Category, Exercise

@app.route("/")
def home():
    return render_template("workouts.html")



@app.route("/body_categories")
def categories():
    return render_template("body_categories.html")


@app.route("/add_body_category", methods=["GET", "POST"])
def add_body_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("body_categories"))
    return render_template("add_body_category.html")
