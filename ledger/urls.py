from django.urls import path
from .views import recipesInDatabase, getRecipe

urlpatterns = [
    path('recipes/list/', recipesInDatabase, name = 'recipebook'),
    path('recipe/<int:num>/', getRecipe, name='getRecipe'),
]

app_name = 'ledger'