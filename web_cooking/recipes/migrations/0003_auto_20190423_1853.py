# Generated by Django 2.2 on 2019-04-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_add_recipe_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_recipe',
            name='file',
        ),
        migrations.AddField(
            model_name='add_recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]