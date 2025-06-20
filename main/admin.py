from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'Category', 'price', 'avilable', 'created', 'updated']

    list_filter = ['avilable', 'created', 'updated', 'Category']
    lsit_editable = ['price', 'avilable']
    prepopulated_fields = {'slug': ('name',)}
  
