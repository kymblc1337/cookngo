from django.db import models

# Create your models here.

class Add_recipe(models.Model):
    title = models.CharField(max_length = 255, help_text ='Название рецепта:')
    description = models.TextField(help_text= 'Описание рецепта')
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    date = models.DateTimeField(auto_now_add = True, auto_now = False)
    image = models.ImageField(blank = True)
