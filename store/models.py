from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )
    description = models.CharField(
        max_length=800,
        verbose_name='Description'
    )
    rating = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name='Rating'
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='stores',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    status = models.CharField(
        choices=(('active', 'Active'), ('deactivated', 'Deactivated'), ('in_review', 'In review')),
        max_length=20,
        default='in_review'
    )
