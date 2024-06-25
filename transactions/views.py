from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Transaction
from .serializers import TransactionSerializer
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import io

from users.permissions import CanViewAllTransactions, CanManageTransactions

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter
    ]
    filterset_fields = ['status', 'transaction_type', 'date', 'category']
    search_fields = ['order__id', 'invoice__id', 'customer__name']
    ordering_fields = ['date', 'amount']
    permission_classes = [CanViewAllTransactions]

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        """
        Exports all filtered transactions to a CSV file.
        """
        transactions = self.filter_queryset(self.get_queryset())
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename="transactions.csv"'
        )
        writer = csv.writer(response)
        writer.writerow([
            'ID', 'Order', 'Invoice', 'Customer', 'Type', 'Category',
            'Amount', 'Date', 'Payment Method', 'Status'
        ])
        for transaction in transactions:
            writer.writerow([
                transaction.id, transaction.order, transaction.invoice,
                transaction.customer, transaction.transaction_type,
                transaction.category, transaction.amount, transaction.date,
                transaction.payment_method, transaction.status
            ])
        return response

    @action(detail=False, methods=['get'])
    def export_pdf(self, request):
        """
        Exports all filtered transactions to a PDF report
        """
        transactions = self.filter_queryset(self.get_queryset())
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 800, "Transactions Report")
        y = 750
        for transaction in transactions:
            p.drawString(100, y, f"{transaction.id} {transaction.order} {transaction.invoice} {transaction.customer} {transaction.transaction_type} {transaction.category} {transaction.amount} {transaction.date} {transaction.payment_method} {transaction.status}")
            y -= 20
        p.showPage()
        p.save()
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = (
            'attachment; filename="transactions.pdf"'
        )
        return response

    @action(detail=False, methods=['post'])
    def bulk_update_status(self, request):
        """
        Updates the status of multiple transactions identified by their IDs.
        """
        status = request.data.get('status')
        ids = request.data.get('ids')
        if status and ids:
            transactions = Transaction.objects.filter(id__in=ids)
            transactions.update(status=status)
            return Response(
                {'message': 'Transactions updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST
        )
