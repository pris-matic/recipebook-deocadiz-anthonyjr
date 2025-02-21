from django.urls import path
from .views import recipebook

urlpatterns = [
    path('recipes/list/', recipebook, name = 'recipebook'),
]

app_name = 'ledger'