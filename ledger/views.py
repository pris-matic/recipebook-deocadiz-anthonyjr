from django.shortcuts import render, redirect
from django.template import loader
from .models import Recipe, RecipeIngredient, RecipeImage, Profile
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

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
    images = RecipeImage.objects.filter(recipe=recipe)
    return render(request, 'recipeNumber.html',{'recipe': recipe, 'ingredients': ingredients, 'images': images})

@login_required
def addRecipe(request):

    if request.method == 'POST':

        recipeForm = RecipeForm(request.POST)
        recipeIngredientForm = RecipeIngredientForm(request.POST)
        
        if recipeForm.is_valid(): 
            try:
                recipe = recipeForm.save(commit=False)
                profile = Profile.objects.get(user = request.user)
                recipeName = recipeForm.cleaned_data.get('name')

                if Recipe.objects.filter(name__iexact=recipeName, author=profile).exists():
                    recipeForm.add_error(None, 'Recipe already exists.')
                else:
                    recipe.name = recipeName
                    recipe.author = profile
                    recipe.save()
                    return redirect('ledger:addRecipe')
            
            except IntegrityError:
                recipeForm.add_error(None, 'Recipe Already Exists')


        if recipeIngredientForm.is_valid():
            try:
                recipeIngredientForm.save()
                return redirect('ledger:recipebook')
            except IntegrityError:
                recipeIngredientForm.add_error(None, 'Recipe Ingredient Already Exists')

    else:
        recipeForm = RecipeForm()
        recipeIngredientForm = RecipeIngredientForm()

    return render(request, 'addRecipe.html', {'recipe': recipeForm, 'recipeIngredient': recipeIngredientForm})

@login_required
def addIngredient(request):

    if request.method == 'POST':

        ingredientForm = IngredientForm(request.POST)
        if ingredientForm.is_valid():
            try:
                ingredientForm.save()
                return redirect('ledger:addRecipe')
            except IntegrityError:
                ingredientForm.add_error(None, 'Ingredient Already Exists')
    
    else:
        ingredientForm = IngredientForm()

    return render(request, 'addIngredient.html', {'ingredient': ingredientForm})

@login_required
def addImage(request,num):
    
    if request.method == 'POST':

        imageForm = RecipeImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            image = imageForm.save(commit=False)
            recipe = Recipe.objects.get(id=num)
            image.recipe = recipe
            image.save()
            return redirect('ledger:getRecipe', num)
    else:
        imageForm = RecipeImageForm()

    return render(request, 'addImage.html', {'image': imageForm})