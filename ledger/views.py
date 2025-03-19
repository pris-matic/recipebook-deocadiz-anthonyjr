from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

@login_required
def recipesInDatabase(request):
    items = Recipe.objects.all()
    return render(request, 'recipebook.html', {'recipes': items})

@login_required
def getRecipe(request,num):
    recipe = Recipe.objects.get(id=num)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'recipeNumber.html',{'recipe': recipe, 'ingredients' : ingredients})