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
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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
