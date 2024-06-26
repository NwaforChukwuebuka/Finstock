from django.db import models
from django.utils import timezone


class StockAdjustment(models.Model):
    """
    Model representing a stock adjustment.
    """
    product = models.ForeignKey(
        'products.Product',
        related_name='stock_adjustments',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    adjusted_by = models.ForeignKey(
        'core.Customer',
        related_name='stock_adjustments',
        on_delete=models.SET_NULL,
        null=True
    )
    adjustment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.adjustment_type.capitalize()} {self.quantity} for {self.product.name}"
