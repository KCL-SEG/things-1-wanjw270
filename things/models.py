from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0, message= 'value can not be less than 0'), MaxValueValidator(100, message='value can not be bigger than 100')], unique=False)