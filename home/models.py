from django.db import models


class products(models.Model):
    name = models.CharField(max_length=100)

