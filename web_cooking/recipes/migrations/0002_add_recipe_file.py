# Generated by Django 2.2 on 2019-04-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_recipe',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
