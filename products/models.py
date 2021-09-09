from django.db import models
from django.db.models.signals import post_save
from django.db.models import Sum
import uuid


class Product(models.Model): 
    title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(max_length=1000, blank=False)
    quantity = models.IntegerField(default=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    
    class Meta:
        verbose_name_plural = "Produkteliai"

    def __str__(self):
        return self.title

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            self.quantity = self.quantity * 100
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.order_number
    
    def updates(self):
        self.summary = 5
        print("the signal is working {}".format(self.summary))

    def duoble(self):
        self.quantity = self.quantity * 200
        self.save()
       

class OrderSummary(models.Model):
    summary = models.CharField(blank=False, null=False, max_length=200)
    delivery_cost = models.DecimalField(blank=False, default=0, null=False, decimal_places=3, max_digits=10)
    vat = models.DecimalField(blank=False, default=0, null=False, decimal_places=3, max_digits=10)

    def calc(self):
        print("This what happend right now")   


    def update_summary(sender, instance, **kwargs):

        summary = Product.quantity
            
        print('The signal was called and the summary is  {}'.format(summary))


    post_save.connect(update_summary, sender=Product)
    
    def updatess(asd):
        calcs = asd.quantity + 111
        OrderSummary.objects.create(summary=10, delivery_cost=calcs, vat = 200)
        print("the signal is working as we cab see".format(asd.quantity))
    
    def __str__(self, *args, **kwargs):
        return self.summary
    

    

    

    
    

    


    
    


