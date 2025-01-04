from flask import render_template, request, redirect, url_for
from workouts import app, db
from workouts.models import Category, Exercise

@app.route("/")
def home():
    return render_template("workouts.html")



@app.route("/body_categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("body_categories.html", categories=categories)


@app.route("/add_body_category", methods=["GET", "POST"])
def add_body_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_body_category.html")


@app.route("/edit_body_category/<int:category_id>", methods=["GET", "POST"])
def edit_body_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_body_category.html", category=category)
