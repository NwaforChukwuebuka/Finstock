from rest_framework import viewsets, permissions
from .models import StockAdjustment
from .serializers import StockAdjustmentSerializer

class StockAdjustmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing stock adjustment instances.
    """
    queryset = StockAdjustment.objects.all()
    serializer_class = StockAdjustmentSerializer
    permission_classes = [permissions.IsAuthenticated]
