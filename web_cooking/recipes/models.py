from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255 )
    def __str__(self):
        return self.title

class Kitchen(models.Model):
    title = models.CharField(max_length = 255)
    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length = 255,help_text ='Название рецепта:')
    description = models.TextField(max_length = 255, help_text= 'Описание рецепта')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank = True, upload_to='recipes_img/')
    category = models.ForeignKey(Category, null = True, blank= True,
                                 on_delete=models.SET_NULL)
    kitchen = models.ForeignKey(Kitchen, null = True, blank= True,
                                on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menu, null = True, blank = True,
                             on_delete = models.SET_NULL)
    def __str__(self):
        return self.title
