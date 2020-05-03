from flask import Flask
from flask import request
from flask import render_template
from A import get_recipe, get_nutrition, print_recipe_nutrition, get_recipe2, get_recipe_url

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')
    

@app.route("/search/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        ingredient_1 = str(request.form["ingredient 1"])
        ingredient_2 = str(request.form["ingredient 2"])
        ingredient_3 = str(request.form["ingredient 3"])
        ingredient_4 = str(request.form["ingredient 4"])

        ingredient = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
        recipes  = get_recipe2(ingredient, 3)
        label_1 = recipes[0]['label']
        label_2 = recipes[1]['label']
        label_3 = recipes[2]['label']

        calories_1 = recipes[0]['calories']
        calories_2 = recipes[1]['calories']
        calories_3 = recipes[2]['calories']        

        cautions_1 = recipes[0]['cautions']
        cautions_2 = recipes[1]['cautions']
        cautions_3 = recipes[2]['cautions']

        if recipes:
            return render_template("results.html", calories_1=calories_1, label_1=label_1)
        else:
            return render_template("search.html", error=True)

    return render_template("search.html", error=None)
