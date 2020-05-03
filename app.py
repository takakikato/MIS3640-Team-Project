from flask import Flask
from flask import request
from flask import render_template
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
        label_1 = recipes[0]['label']
        calories_1 = recipes[0]['calories']
        url = get_recipe_url(ingredient, 3)
        url_1 = url[0]
        if recipes:
            return render_template("results.html", url=url, calories_1=calories_1, label_1=label_1)
        else:
            return render_template("results.html", error=True)

    return render_template("results.html", error=None)
