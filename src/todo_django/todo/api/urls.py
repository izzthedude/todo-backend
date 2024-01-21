from django.urls import path

from todo_django.todo.api.views import (
    CategoryDetailView,
    CategoryListView,
    ItemDetailView,
    ItemListView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),
    path("todos/", ItemListView.as_view()),
    path("todos/<int:pk>/", ItemDetailView.as_view()),
]
