# admin.py
from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'named_url', 'parent', 'menu')
    list_filter = ('menu',)