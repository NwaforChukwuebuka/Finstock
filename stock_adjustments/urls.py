from django.urls import path
from . import views

urlpatterns = [
    path('stock_adjustments/', views.StockAdjustmentListCreateAPIView.as_view(), name='stock_adjustment_list_create'),
    path('stock_adjustments/<int:pk>/', views.StockAdjustmentRetrieveUpdateDestroyAPIView.as_view(), name='stock_adjustment_detail'),
    # Add more paths as needed for your application
]
