# MIS3640-Team-Project
Repository for team project for python class. 
This webapp will allow for a user to input any ingredients they wish to cook with. The app will then reccomend a recipie using those ingredients.

Requirements:  
Modules - requests, flask   
API - id and key for Edamam Nutrition Analysis and Receipe Search APIs  

Documentations for the APIs:  
Nutrition Analysis - https://developer.edamam.com/edamam-docs-nutrition-api  
Recipe Search - https://developer.edamam.com/edamam-docs-recipe-api  

Usage:  
1. recipe.py  
get_recipe, get_nutrition - return raw output from EDAMAM API  
get_recipe2, get_recipe_nutrition - returns cleaned infromation  
print_recipe, print_recipe_nutrition, print_nutrition - prints formatted information  
(view docstrings for more detailed usage)  
2. app.py  
runs interactive application that displays recipes, and nutritional values based on ingredient input    