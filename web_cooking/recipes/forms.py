from django import forms
from .models import Add_recipe

User = Add_recipe



class Add_recipe_form(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'title',
            'description',
            'image',
            'diff',
        ]
