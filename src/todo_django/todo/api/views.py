from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from todo_django.todo.api.serializers import CategorySerializer, ItemSerializer
from todo_django.todo.models import Category, Item


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # PUT enforces required fields, but PATCH doesn't, so I'm "redirecting" the PUT
        # behaviour to PATCH
        return super().patch(request, *args, **kwargs)
