from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, OrderSummary


@receiver(post_save, sender=Product)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.updates()