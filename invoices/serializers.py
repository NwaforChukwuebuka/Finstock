from rest_framework import serializers
from .models import Invoice, InvoiceItem


class InvoiceItemSerializer(serializers.ModelSerializer):
    """
    Serializer for InvoiceItem model.
    """

class Meta:
    model = InvoiceItem
    fields = ['description', 'quantity', 'unit_price']


class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Invoice model.
    """
    items = InvoiceItemSerializer(many=True, read_only=True)


class Meta:
    model = Invoice
    fields = ['id', 'customer', 'project', 'date', 'items', 'total_amount']
