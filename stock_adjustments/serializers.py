from rest_framework import serializers
from .models import StockAdjustment

class StockAdjustmentSerializer(serializers.ModelSerializer):
    """
    Serializer for StockAdjustment model.
    """

    class Meta:
        model = StockAdjustment
        fields = '__all__'
