from flask import Flask
from flask import request
from flask import render_template
from A import get_recipe, get_nutrition, print_recipe_nutrition, get_recipe2, get_recipe_nutrition

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome_2.html')
    

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

        calories_1 = int(recipes[0]['calories'])
        calories_2 = int(recipes[1]['calories'])
        calories_3 = int(recipes[2]['calories'])        


        cautions_1 = ', '.join(recipes[0]['cautions'])
        cautions_2 = ', '.join(recipes[1]['cautions'])
        cautions_3 = ', '.join(recipes[2]['cautions'])

        dietLabels_1 = ', '.join(recipes[0]['dietLabels'])
        dietLabels_2 = ', '.join(recipes[1]['dietLabels'])
        dietLabels_3 = ', '.join(recipes[2]['dietLabels'])

        healthLabels_1 = ', '.join(recipes[0]['healthLabels'])
        healthLabels_2 = ', '.join(recipes[1]['healthLabels'])
        healthLabels_3 = ', '.join(recipes[2]['healthLabels'])

        ingredientLines_1 = ', '.join(recipes[0]['ingredientLines'])
        ingredientLines_2 = ', '.join(recipes[1]['ingredientLines'])
        ingredientLines_3 = ', '.join(recipes[2]['ingredientLines'])

        url_1 = recipes[0]['url']
        url_2 = recipes[1]['url']
        url_3 = recipes[2]['url']

        image_1 = recipes[0]['image']
        image_2 = recipes[1]['image']
        image_3 = recipes[2]['image']


        if recipes:
            return render_template("results.html", calories_1=calories_1, calories_2=calories_2, calories_3=calories_3, label_1=label_1, label_2=label_2,
            label_3=label_3, cautions_1=cautions_1, cautions_2=cautions_2, cautions_3=cautions_3, dietLabels_1=dietLabels_1, dietLabels_2=dietLabels_2, dietLabels_3=dietLabels_3,
            healthLabels_1=healthLabels_1, healthLabels_2=healthLabels_2, healthLabels_3=healthLabels_3, ingredientLines_1=ingredientLines_1, ingredientLines_2=ingredientLines_2,
            ingredientLines_3=ingredientLines_3, url_1=url_1, url_2=url_2, url_3=url_3, image_1=image_1, image_2=image_2, image_3=image_3)
        else:
            return render_template("search.html", error=True)

    return render_template("search.html", error=None)


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500

@app.errorhandler(400)
def page_not_found(e):
    return render_template('error.html'), 400