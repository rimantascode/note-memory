from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Product, OrderSummary


@receiver(pre_save, sender=Product)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem update/create
    """
    OrderSummary.updatess(instance)