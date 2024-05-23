from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            "%(value)s is not an even number",
            params={"value": value},
        )


class Project(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120), validate_even]
    )

    def clean(self):
        if self.number == 10:
            raise ValidationError("number cannot be 10")


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
