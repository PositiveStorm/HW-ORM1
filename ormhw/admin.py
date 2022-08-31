from django.contrib import admin

from .models import Element

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'price']