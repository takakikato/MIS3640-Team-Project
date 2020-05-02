from flask import Flask, render_template, request
import requests
from A import get_recipe, get_nutrition, print_recipe_nutrition

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/search/", methods=["GET", "POST"])
def recipe_search():
    if request.method == "POST":
        ingredient = str(request.form["ingredient"])
        ingredient,  = get_recipe(location)


        if station_name:
            return render_template("results.html", )
        else:
            return render_template("results.html", error=True)

    return render_template("results.html", error=None)
