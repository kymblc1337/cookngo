from django.contrib import admin
from .models import *
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display =  ["title","updated", "date"]
    list_filter = ["updated"]
    search_fields = ["title"]
    class Meta:
        model = Add_recipe

admin.site.register(Add_recipe, RecipeAdmin)