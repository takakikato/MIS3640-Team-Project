import requests
from pprint import pprint

def get_json(url, parameters):
    '''
    '''
    return requests.get(url, params=parameters).json()


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


def main():
    get_recipe('salmon')


if __name__ == "__main__":
    main()
