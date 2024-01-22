from collections import OrderedDict
from typing import Any

from rest_framework import serializers
from rest_framework.serializers import ReturnDict

from todo_django.todo.models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryField(serializers.PrimaryKeyRelatedField):
    """
    This field makes it so that you can GET the Category object, but POST with just
    a Category's ID.
    """

    def to_representation(self, value: int) -> ReturnDict | None:
        pk = super().to_representation(value)

        try:
            item = Category.objects.get(pk=pk)
            serializer = CategorySerializer(item)
            return serializer.data

        except Category.DoesNotExist:
            return None

    def get_choices(
        self,
        cutoff: int | None = None,
    ) -> dict[Any, str] | OrderedDict[Any, str]:
        queryset = self.get_queryset()
        if queryset is None:
            return {}
        return OrderedDict([(item.id, str(item)) for item in queryset])


class ItemSerializer(serializers.ModelSerializer):
    category = CategoryField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Item
        fields = "__all__"
