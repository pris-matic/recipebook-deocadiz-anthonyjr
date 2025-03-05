from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Recipe, RecipeIngredient

# Create your views here.

def recipesInDatabase(request):
    items = Recipe.objects.all()
    return render(request, 'recipebook.html', {'recipes': items})

def getRecipe(request,num):
    recipe = Recipe.objects.get(id=num)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'recipeNumber.html',{'recipe': recipe, 'ingredients' : ingredients})