from django.db import models

# Create your models here.

class Add_recipe(models.Model):
    title = models.CharField(max_length=255, help_text='Название рецепта:')
    description = models.TextField(help_text='Описание рецепта')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(upload_to='articles/', width_field=100,height_field=100)
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title