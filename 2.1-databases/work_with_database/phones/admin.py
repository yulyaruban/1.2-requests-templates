from django.contrib import admin
from .models import Phone

# Register your models here.
# @admin.register(Phone)
# class PhoneAdmin 

class ArticleAdmin(admin.ModelAdmin):
    slug = {"slug": ["name"]}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}