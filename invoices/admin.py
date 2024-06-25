from django.contrib import admin
from .models import Invoice, InvoiceItem


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """
    This class configures the admin interface for the Invoice model.
    """
    list_display = (
        'invoice_number', 'customer', 'issue_date', 'due_date',
        'paid', 'created', 'modified'
    )
    search_fields = (
        'invoice_number', 'customer__first_name', 'customer__last_name',
        'customer__email'
    )
    list_filter = ('paid', 'issue_date', 'due_date')


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    """
    This class configures the admin interface for the InvoiceItem model.
    """
    list_display = ('invoice', 'description', 'quantity', 'unit_price')
    search_fields = ('description',)
    list_filter = ('invoice',)
