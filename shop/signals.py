from .models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

@receiver(post_save, sender=Product)
def my_handler(sender, **kwargs):
    cache.clear()