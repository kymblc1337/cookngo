from django.db import models

# Create your models here.

class Add_recipe(models.Model):
    title = models.CharField(max_length=255, help_text='Название рецепта:')
    description = models.TextField(help_text='Описание рецепта')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(upload_to='articles/')
    DIFFICULTY = (
        ('1','1'),
        ('2', '2'),
        ('3','3'),
        )
    RATE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    diff = models.IntegerField(choices=DIFFICULTY, null = True)
    rat = models.IntegerField(choices=RATE, null = True)
    likes = models.IntegerField(default='0')
    dislikes = models.IntegerField(default='0')
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title