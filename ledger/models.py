from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='uniqueIngredient')]

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:getRecipe',args=[self.pk])
    
    class Meta:
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name','author'], name='uniqueNamePerAuthor')]


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ingredient.name} - {self.quantity}'
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['recipe','ingredient'], name='uniqueIngredientPerRecipe')]

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/',null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('ledger:addImage',args=[self.recipe.pk])

    def __str__(self):
        return f'{self.recipe.name} image'