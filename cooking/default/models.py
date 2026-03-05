from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    pass

class Ingredient(models.Model):
    ingredient_name=models.CharField(max_length=100)
    ingredient_measurement=models.CharField(max_length=100)

class Direction(models.Model):
    recipe_direction=models.TextField(default="")

class cooking_recipe(models.Model): #how to get django models to accept a list, key value pairs --maybe foreign keys?
    title=models.CharField(max_length=64)
    description=models.TextField(default="")
    ingredients=models.ManyToManyField(Ingredient, related_name="ingredients", null=True, blank=True)
    directions=models.ManyToManyField(Direction, related_name="directions", null=True, blank=True)
    user_published=models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_published")
    date=models.DateField(null=True)
    
    image=models.ImageField(null=True,  blank=True)#subdirectory files will be uploaded to
    #->uploaded will be a link=> html= <img src={{asdf.image}} />
    

