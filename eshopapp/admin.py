from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)



