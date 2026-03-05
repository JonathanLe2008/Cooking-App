from django import forms
from .models import *
from django.forms import ModelForm


class cooking_recipe_form(ModelForm):

    class Meta:
        model = cooking_recipe
        fields = ['title', 'image']
        # ingredients=forms.ModelMultipleChoiceField(
        #     queryset=Ingredient.objects.all(),
        #     widget=forms.CheckboxSelectMultiple   
        # ) 
        # directions=forms.ModelMultipleChoiceField(
        #     queryset=Ingredient.objects.all(),
        #     widget=forms.CheckboxSelectMultiple   
        # )
