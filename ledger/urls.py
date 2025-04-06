from django.urls import path
from .views import recipesInDatabase, getRecipe, homepage, addRecipe,addIngredient,addImage

urlpatterns = [
    path('home/', homepage, name='home'),
    path('recipes/list/', recipesInDatabase, name = 'recipebook'),
    path('recipe/<int:num>/', getRecipe, name='getRecipe'),
    path('recipe/add/', addRecipe, name='addRecipe'),
    path('recipe/add/ingredient', addIngredient, name='addIngredient'),
    path('recipe/<int:num>/add_image', addImage, name='addImage'),
]

app_name = 'ledger'