import requests
from pprint import pprint


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
    parameters = {'app_id': 'ef73e741', 'app_key': '687e39d9619e78a7956d715af8585b7b', 'q': ingredient, 'from': start, 'to': end}
    url = 'https://api.edamam.com/search'

    return get_json(url, parameters)['hits']

pprint(get_recipe(['1 cup rice', '5 shrimps', '2 eggs', 'half carrot', '150g chicken '],3))

def get_recipe2(ingredient, end):
    response = get_recipe(ingredient, end)

    recipes = []
    keys = ['label', 'calories', 'cautions', 'dietLabels', 'healthLabels', 'ingredientLines']

    for recipe in response:
        dic = recipe['recipe']
        sub = {key: dic[key] for key in keys}
        recipes.append(sub)

    return recipes

def get_recipe_url(ingredient, end):
    response = get_recipe(ingredient, end)
    url_r = []
    for recipe in response:
        url_r.append(recipe['recipe']['url'])
    return url_r

def get_calories(ingredient, end):
    response = get_recipe(ingredient, end)
    calories = []
    for recipe in response:
        calories.append(recipe['recipe']['calories'])
    return calories

