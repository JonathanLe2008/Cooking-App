from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from datetime import datetime
import numpy as np
import random

# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("view_recipes"))
        else:
            return render(request, "default/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "default/login.html")
    
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("view_recipes"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "default/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "default/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("view_recipes"))
    else:
        return render(request, "default/register.html")
    
def view_recipes(request):
    recipe_list=cooking_recipe.objects.all()
    return render(request, "default/view_recipes.html",{"recipes":recipe_list})

def view_recipe_details(request, id):
    recipe=cooking_recipe.objects.get(pk=id)
    image=recipe.image
    current_user=request.user==recipe.user_published
    return render(request, "default/view_recipes.html",     
        {"user":current_user, "recipe": recipe, "image":image, "ingredients": recipe.ingredients.all(), "directions": recipe.directions.all()}
        )

def search_recipes(request):
    if request.method=="POST":
        text=request.POST['search_bar']
        recipes_returned=[]
        for x in cooking_recipe.objects.all():
            if text.lower() in x.title.lower():
                recipes_returned.append(x)

        return render(request, "default/search_recipes.html", {'Searched': True, "recipes": recipes_returned})
    else:
        return render(request, "default/search_recipes.html", {'Searched': False})

def create_recipes(request):
    if request.method=="POST":
        
        #directions and ingredients
        ingr_list=request.POST["ingredients_list_hidden"].split(",")
        mesaurements_list=request.POST["ingredients_measurements_hidden"].split(",")
        directions_list=request.POST["directions_hidden"].split(",")
        description=request.POST["recipe_description"]
        form=cooking_recipe_form(request.POST, request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            image=form.cleaned_data['image']
        user=request.user
        current_date=datetime.now()
        temp=cooking_recipe.objects.create(title=title, description=description, image=image, user_published=user, date=current_date)
        # print(temp.id)
        # print(mesaurements_list)
        # print(ingr_list)
        # print(directions_list)
        
        #reading in the ingr/directions as chars

        for i in range(len(ingr_list)):
            one=Ingredient.objects.create(ingredient_name=ingr_list[i], ingredient_measurement=mesaurements_list[i])
            temp.ingredients.add(one)
        for i in range(len(directions_list)):
            one=(Direction.objects.create(recipe_direction=directions_list[i]))
            temp.directions.add(one)



        return HttpResponseRedirect(reverse("view_recipes"))
    else:
        form=cooking_recipe_form()
        return render(request, "default/create_recipes.html", {'form':form})
    
def user_recipes(request):
    user=request.user
    recipes=[]
    for x in cooking_recipe.objects.all():
        if x.user_published==user:
            recipes.append(x)
    return render(request,"default/user_recipes.html",{
        "recipes": recipes
    })

def random_recipe(request):
    # print(1)
    temp=cooking_recipe.objects.all()
    if len(temp) is not 0:
        random_id=(random.randint(temp.first().id, temp.last().id))
        return view_recipe_details(request, random_id)
    else:
        return view_recipes(request)
    # return HttpResponseRedirect(reverse("view_recipes"))

def edit_recipe(request,id):
    if request.method=="POST":
        
        recipe=cooking_recipe.objects.get(pk=id).delete()
        ingr_list=request.POST["ingredients_list_hidden"].split(",")
        mesaurements_list=request.POST["ingredients_measurements_hidden"].split(",")
        directions_list=request.POST["directions_hidden"].split(",")
        description=request.POST["recipe_description"]
        form=cooking_recipe_form(request.POST, request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            image=form.cleaned_data['image']
        user=request.user
        current_date=datetime.now()
        temp=cooking_recipe.objects.create(title=title, description=description, image=image, user_published=user, date=current_date)
        # print(temp.id)
        # print(mesaurements_list)
        # print(ingr_list)
        # print(directions_list)
        
        #reading in the ingr/directions as chars

        for i in range(len(ingr_list)):
            one=Ingredient.objects.create(ingredient_name=ingr_list[i], ingredient_measurement=mesaurements_list[i])
            temp.ingredients.add(one)
        for i in range(len(directions_list)):
            one=(Direction.objects.create(recipe_direction=directions_list[i]))
            temp.directions.add(one)
        

        
        user=request.user
        recipes=[]
        for x in cooking_recipe.objects.all():
            if x.user_published==user:
                recipes.append(x)
        return render(request,"default/user_recipes.html",{
            "recipes": recipes
        })
    else:
        recipe=cooking_recipe.objects.get(pk=id)
        form=cooking_recipe_form(initial={'title': recipe.title})
        current_iamge=recipe.image

        directions=recipe.directions.all()
        ingredients=recipe.ingredients.all()
        return render(request, "default/user_recipes.html",     
        {"editing":True,"form": form, "recipe": recipe, "directions": directions, "ingredients": ingredients, "id":id, "current_image":current_iamge}
        )
    
def delete_recipe(request, id):
    cooking_recipe.objects.get(pk=id).delete()
    return render(request, "default/view_recipes.html")
