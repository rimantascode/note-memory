from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(max_length=1000, blank=False)
    quantity = models.IntegerField(default=False)


