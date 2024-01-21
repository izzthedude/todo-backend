from django_filters import rest_framework as filters

from todo_django.todo.models import Item


class ItemSearchFilter(filters.FilterSet):
    q = filters.CharFilter(field_name="todo", lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ("todo",)
