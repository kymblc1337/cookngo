from django import forms
from .models import Recipe
# -*- coding:utf-8 -*-





class Add_recipe_form(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'image',
            'diff',
            'kitchen',
            'category',
        ]

        labels = {
            'title': 'Название рецепта:',
            'description': 'Описание рецепта:',
            'image': 'Фотография рецепта:',
            'diff': 'Сложность рецепта:',
            'kitchen': 'Кухня:',
            'category': 'Категория блюда:'


        }

        def __init__(self, *args, **kwargs):
            super(Add_recipe_form, self).__init__(*args, **kwargs)
            self.fields['title'].label = 'kmllmk'
            self.fields['description'].label = 'kmllmk'
            self.fields['image'].label = 'kmllmk'
            self.fields['diff'].label = 'kmllmk'
