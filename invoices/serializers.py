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
    total_amount = serializers.SerializerMethodField()


    class Meta:
        model = Invoice
        fields = ['id', 'customer', 'items', 'total_amount']

    def get_total_amount(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.quantity * item.unit_price
        return total
