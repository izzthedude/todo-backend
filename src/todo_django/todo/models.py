from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=32,
        validators=[
            MinLengthValidator(1, "The 'name' field must contain at least 1 character.")
        ],
    )

    @classmethod
    def get_default_pk(cls) -> int:
        category, created = cls.objects.get_or_create(name="None")
        return category.pk

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Item(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        default=Category.get_default_pk,
        on_delete=models.SET_DEFAULT,
        related_name="items",
    )
    todo = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(1, "The 'todo' field must contain at least 1 character.")
        ],
    )
    completed = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return self.todo
