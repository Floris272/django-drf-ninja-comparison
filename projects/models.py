from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.exceptions import ValidationError


class Project(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )

    def clean(self):
        if self.number == 10:
            raise ValidationError("number cannot be 10")


class Employee(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
