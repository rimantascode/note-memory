from django.db import models


class Product(models.Model): 
    title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(max_length=1000, blank=False)
    quantity = models.IntegerField(default=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def get_friendly_name(self):
        return self.friendly_name
    
    


