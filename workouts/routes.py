from flask import render_template
from workouts import app, db
from workouts.models import Category, Exercise

@app.route("/")
def home():
    return render_template("workouts.html")