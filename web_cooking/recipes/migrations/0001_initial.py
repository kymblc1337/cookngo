# Generated by Django 2.2 on 2019-04-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название рецепта:', max_length=255)),
                ('description', models.TextField(help_text='Описание рецепта', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]