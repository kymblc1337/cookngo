from django.db import models

# Create your models here.

class add_recipe(models.Model):
    title = models.CharField(max_length = 255, help_text ='Название рецепта:')
    description = models.TextField(max_length = 255, help_text= 'Описание рецепта')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank = True)
