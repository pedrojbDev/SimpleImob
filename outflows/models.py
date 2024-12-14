from django.db import models
from inventory.models import Inventory

class Outflow(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT,related_name='outflows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.inventory)
