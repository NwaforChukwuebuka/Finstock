from django.db import models
from core.models import TimeStampedModel, Customer, Order
from invoices.models import Invoice


class Transaction(TimeStampedModel):
    """
    Model representing a financial transaction.
    """
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
        ('other', 'Other'),
    )

    TRANSACTION_STATUSES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded'),
        ('canceled', 'Canceled'),
    )

    CATEGORY_CHOICES = (
        ('salary', 'Salary'),
        ('marketing_expenses', 'Marketing Expenses'),
        ('office_supplies', 'Office Supplies'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    )

    order = models.ForeignKey(
        Order, related_name='transactions',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    invoice = models.ForeignKey(
        Invoice, related_name='transactions',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    customer = models.ForeignKey(
        Customer, related_name='transactions',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUSES)

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type} \
                - {self.amount}"
