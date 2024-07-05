from django.db import models
from core.models import TimeStampedModel, Customer


class Invoice(TimeStampedModel):
    """
    Model representing an invoice.
    """
    customer = models.ForeignKey(
        Customer, related_name='invoices', on_delete=models.CASCADE
    )
    invoice_number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer}"


class InvoiceItem(models.Model):
    """
    Model representing an item within an invoice.
    """
    invoice = models.ForeignKey(
        Invoice, related_name='items', on_delete=models.CASCADE
    )
    description = models.CharField(max_length=191)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.quantity} x {self.unit_price}"

    def total_price(self):
        return self.quantity * self.unit_price
