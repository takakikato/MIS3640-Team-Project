from flask import Flask, render_template, request
import requests
from A import get_recipe, get_nutrition, print_recipe_nutrition, get_recipe2, get_recipe_url

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/search/", methods=["GET", "POST"])
def recipe_search():
    if request.method == "POST":
        ingredient = str(request.form["ingredient"])
        recipes  = get_recipe2(ingredient, 3)
        url = get_recipe_url(ingredient, 3)
        if recipes:
            return render_template("results.html", url=url, recipe=recipe)
        else:
            return render_template("results.html", error=True)

    return render_template("results.html", error=None)
