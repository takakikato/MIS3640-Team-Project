import requests
from pprint import pprint

recipe_id, recipe_key, nutrition_id, nutrition_key = 'recipe_id', 'recipe_key', 'nutrition_id', 'nutrition_key' 

def get_json(url, parameters):
    '''
    url: string
    parameters: dictionary

    Given a properly formatted url and parameters for a JSON web API request, 
    return a Python JSON object containing the response to that request.
    '''
    return requests.get(url, params=parameters).json()


def post_json(url, parameteres, json, header):
    '''
    url: string
    parameters: dictionary
    json: JSON object / dictionary
    header: dictionary

    Given a properly formatted url, parameters, json, and header for a JSON web API request, 
    return a Python JSON object containing the response to that request.
    '''
    return requests.post(url, params=parameteres, json=json, headers=header).json()


def get_recipe(ingredient, end, start = 0):
    '''
    ingredient: string
    end: integer
    start: integer

    Given a string containing ingredients, return JSON object containing the recipes that include given ingredients.
    Retrun number of recipes between start and end.
    '''
    parameters = {'app_id': recipe_id, 'app_key': recipe_key, 'q': ingredient, 'from': start, 'to': end}
    url = 'https://api.edamam.com/search'

    return get_json(url, parameters)['hits']


def get_recipe2(ingredient, end):
    '''
    ingredient: string
    end: integer

    Given a string containing ingredients, returns properly formatted recipes that include given ingredients.
    Retruns end numbers of recipes.
    '''
    response = get_recipe(ingredient, end)

    recipes = []
    keys = ['label', 'calories', 'cautions', 'dietLabels', 'healthLabels', 'ingredientLines', 'url', 'image']

    for recipe in response:
        dic = recipe['recipe']
        sub = {key: dic[key] for key in keys}
        recipes.append(sub)

    return recipes



def get_recipe_nutrition(ingredient, choice):
    '''
    ingredient: string
    choice: integer

    Given a string containing ingredients, returns properly formatted nutritional facts for chosen recipe.
    '''
    response = get_recipe(ingredient, choice, choice-1)[0]['recipe']
  
    # # 1. dictionary format
    # keys = ['label', 'daily', 'total', 'unit']
    # keys2 = ['label', 'calories', 'cautions', 'dietLabels', 'healthLabels']
    # nutritions = {key: response[key] for key in keys2}
    # nutritions['nutrition'] = []

    # for nutrition in response['digest']:
    #     sub = {key: nutrition[key] for key in keys}
    #     nutritions['nutrition'].append(sub)
    # # format -> {calories, cautions, dietlabels, healthlabels, label, nutrition:[{daily, label, total, unit} for each of nutrient]}


    # # 2. list of strings format
    # nutritions = []
    # for nutrition in response['digest']:
    #     string = f"{nutrition['label']}: {nutrition['total']:.2f}{nutrition['unit']} {nutrition['daily']:.2f}%"
    #     nutritions.append(string)
    # nutritions = [response['label'], response['calories'], ', '.join(response['cautions']), ', '.join(response['dietLabels']), ', '.join(response['healthLabels']), nutritions]
    # # format -> [label, calories, cautions, dietlabels, healthlabels, string list of nutritions]


    # 3. list of list format
    nutritions = []
    for nutrition in response['digest']:
        string = []
        string.extend([nutrition['label'], f"{nutrition['total']:.2f}{nutrition['unit']}", f"{nutrition['daily']:.2f}%"])
        nutritions.append(string)
    
    nutritions = [response['label'], response['calories'], ', '.join(response['cautions']), ', '.join(response['dietLabels']), ', '.join(response['healthLabels']), nutritions]
    # format -> [label, calories, cautions, dietlabels, healthlabels, list of list nutrients]

    return nutritions


def print_recipe(ingredient, end):
    '''
    ingredient: string
    end: integer

    Given a string containing ingredients, prints properly formatted recipes that include given ingredients.
    Retruns end numbers of recipes.
    '''
    response = get_recipe(ingredient, end)

    for i, recipe in enumerate(response):
        print(f"{i+1}. {recipe['recipe']['label']} ({recipe['recipe']['calories']:.2f} cal)")
        print(f"Caution: {', '.join(recipe['recipe']['cautions'])} | Diet: {'. '.join(recipe['recipe']['dietLabels'])} | Health: {', '.join(recipe['recipe']['healthLabels'])}")
        print("Ingredients:")
        for ingredient in recipe['recipe']['ingredientLines']:
            print(f'  \u2022 {ingredient}')
        print(recipe['recipe']['image'])
        print('\n')     


def print_recipe_nutrition(ingredient, choice):
    '''
    ingredient: string
    choice: integer

    Given a string containing ingredients, prints properly formatted nutritional facts for chosen recipe.
    '''
    response = get_recipe(ingredient, choice, choice-1)
        
    print(f"{choice}. {response[0]['recipe']['label']:<44} Calories {response[0]['recipe']['calories']:>7.2f}")
    print('----------------------------------------------------------------')
    print('Nutrient                              Total        % Daily Value')
    print('----------------------------------------------------------------')
    for nutrient in response[0]['recipe']['digest']:
        print(f"{nutrient['label']:<30} {nutrient['total']:>10.2f} {nutrient['unit']:<5}{nutrient['daily']:>15.2f} %")
        if 'sub' in nutrient:
            for sub_nutrient in nutrient['sub']:
                print(f"  {sub_nutrient['label']:<28} {sub_nutrient['total']:>10.2f} {sub_nutrient['unit']:<5}{sub_nutrient['daily']:>15.2f} %")  
        if nutrient['label'] == 'Protein':
            print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')
    

def get_nutrition(title, ingredient):
    '''
    title: string
    ingr: list

    Given title of the recipe, and list of ingredients, returns JSON object containing nutritional fact of the recipe.
    '''
    parameteres = {'app_id': nutrition_id, 'app_key': nutrition_key}
    json = {'title': title, 'ingr': ingredient}
    header = {'Content-type': 'application/json'}
    url = 'https://api.edamam.com/api/nutrition-details'

    return post_json(url, parameteres, json, header)


def print_nutrition(title, ingredient):
    '''
    title: string
    ingredient: list

    Given title of the recipe and list of ingredients, prints properly formatted nutrional facts of the recipe
    '''
    response = get_nutrition(title, ingredient)

    daily = response['totalDaily']
    total = response['totalNutrients']

    print(title)
    print(f"Caution: {', '.join(response['cautions'])} | Diet: {'. '.join(response['dietLabels'])} | Health: {', '.join(response['healthLabels']).replace('_', '-')}")
    print('Ingredients:')
    for item in ingredient:
        print(f'  \u2022 {item}')   
    print('\n')
    print('Nutrient                              Total        % Daily Value')
    print('----------------------------------------------------------------')
    for nutrient in daily:
        print(f"{daily[nutrient]['label']:<30} {total[nutrient]['quantity']:>10.2f} {total[nutrient]['unit']:<5}{daily[nutrient]['quantity']:>15.2f} %")
        if daily[nutrient]['label'] == 'Energy' or daily[nutrient]['label'] == 'Protein':
            print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')
    


def main():
    # pprint(get_recipe2('fried rice', 3))

    # pprint(get_recipe_nutrition('fried rice', 3))
    # pprint(get_recipe_nutrition(['1 cup rice', '5 shrimps', '2 eggs', 'half carrot', '150g chicken '],3))

    # print_recipe('Fried Rice', 3)
    # print_recipe_nutrition('Fried Rice', 3)

    # title = 'Takaki Fried Rice'
    # ingredient = ['1 cup rice', '5 shrimps', '2 eggs', 'half carrot', '150g chicken ']
    # print_nutrition(title, ingredient)
    pass

if __name__ == '__main__':
    main()
