import requests
from pprint import pprint

def get_json(url, parameters):
    '''
    '''
    return requests.get(url, params=parameters).json()


def post_json(url, parameteres, json, header):
    '''
    '''
    return requests.post(url, params=parameteres, json=json, headers=header).json()


def get_recipe(ingredient):
    '''
    '''
    parameters = {'app_id': 'ef73e741', 'app_key': '687e39d9619e78a7956d715af8585b7b', 'q': ingredient, 'to': 3}
    url = 'https://api.edamam.com/search'

    response = get_json(url, parameters)['hits']
    for item in response:
        print(item['recipe']['label'])
        print(item['recipe']['ingredientLines'])
        print('\n')


def get_nutrition(title, ingredient):
    '''
    '''
    parameteres = {'app_id': '366257d2', 'app_key': 'd01df5907c09a9b04ba0dd4c0d0ef652'}
    json = {'title': title, 'ingr': ingredient}
    header = {'Content-type': 'application/json'}
    url = 'https://api.edamam.com/api/nutrition-details'

    return post_json(url, parameteres, json, header)

def main():
    get_recipe('salmon')
    title = 'Steamed Salmon'
    ingredient = ['1 center-cut boneless salmon fillet (4 ounces), skin on', 'Lemon wedge, for serving']
    pprint(get_nutrition(title, ingredient))


if __name__ == "__main__":
    main()
