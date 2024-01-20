from django.contrib import admin

from todo_django.todo.models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
