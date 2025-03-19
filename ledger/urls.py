from django.urls import path
from .views import recipesInDatabase, getRecipe, homepage

urlpatterns = [
    path('home/', homepage, name='home'),
    path('recipes/list/', recipesInDatabase, name = 'recipebook'),
    path('recipe/<int:num>/', getRecipe, name='getRecipe'),
]

app_name = 'ledger'