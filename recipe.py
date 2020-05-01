import urllib.request
import requests
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)


# Your API KEYS (you need to use your own keys - very long random characters)
RECIPE_APP_ID = "514ef3ff"
RECIPE_APP_KEY = "8ee308c4bae89de54b4e1d547fb0d7c7"
NUTRITION_APP_KEY = "d01df5907c09a9b04ba0dd4c0d0ef652"
NUTRITION_APP_ID = "366257d2"

URL = f"https://api.edamam.com/search?app_id=${RECIPE_APP_ID}&app_key=${RECIPE_APP_KEY}&from=0&to=3&calories=591-722&health=alcohol-free"

N_URL = f"https://api.edamam.com/api/nutrition-details?app_id=${NUTRITION_APP_ID}&app_key=${NUTRITION_APP_KEY}"



def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

pprint(get_json(URL))


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
    pass

def main():
    get_recipe('salmon')


if __name__ == "__main__":
    main()
