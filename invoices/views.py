from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer
from users.permissions import CanViewAllInvoices, CanManageInvoices
from core.models import Customer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving, updating,
    and deleting invoices.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, CanViewAllInvoices]

    @action(detail=True, methods=['get'], permission_classes=[CanViewAllInvoices])
    def generate_pdf(self, request, pk=None):
        """
        Generates a detailed PDF of the invoice.
        """
        invoice = self.get_object()
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        # Invoice Header
        elements.append(Paragraph("Company Name", styles['Title']))
        elements.append(Paragraph("Company Address", styles['Normal']))
        elements.append(Paragraph("Company Phone Number", styles['Normal']))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Invoice Number: {invoice.id}", styles['Normal']))
        elements.append(Paragraph(f"Invoice Date: {invoice.date}", styles['Normal']))
        elements.append(Spacer(1, 12))

        # Customer Information
        if invoice.customer:
            elements.append(Paragraph("Bill To:", styles['Heading2']))
            elements.append(Paragraph(f"Name: {invoice.customer.name}", styles['Normal']))
            elements.append(Paragraph(f"Address: {invoice.customer.billing_address}", styles['Normal']))
            elements.append(Paragraph(f"Phone: {invoice.customer.phone}", styles['Normal']))
            elements.append(Paragraph(f"Email: {invoice.customer.email}", styles['Normal']))
            elements.append(Spacer(1, 12))

        # Invoice Details
        elements.append(Paragraph(f"Due Date: {invoice.due_date}", styles['Normal']))
        elements.append(Paragraph(f"Payment Terms: {invoice.payment_terms}", styles['Normal']))
        elements.append(Paragraph(f"Tax Rate: {invoice.tax_rate}%", styles['Normal']))
        elements.append(Paragraph(f"Tax Amount: {invoice.tax_amount}", styles['Normal']))
        elements.append(Spacer(1, 12))

        # Invoice Items Table
        elements.append(Paragraph("Invoice Items:", styles['Heading2']))
        data = [
            ["Item Description", "Quantity", "Unit Price", "Line Total"]
        ]
        for item in invoice.items.all():
            data.append([item.description, item.quantity, item.unit_price, item.quantity * item.unit_price])

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        # Invoice Summary
        elements.append(Paragraph("Invoice Summary:", styles['Heading2']))
        elements.append(Paragraph(f"Subtotal: {invoice.subtotal}", styles['Normal']))
        elements.append(Paragraph(f"Tax Amount: {invoice.tax_amount}", styles['Normal']))
        elements.append(Paragraph(f"Total Amount: {invoice.total_amount}", styles['Normal']))

        doc.build(elements)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
        return response

    @action(detail=True, methods=['post'], permission_classes=[CanManageInvoices])
    def mark_as_paid(self, request, pk=None):
        """
        Marks the invoice as paid.
        """
        invoice = self.get_object()
        invoice.status = 'paid'
        invoice.save()
        return Response({'status': 'Invoice marked as paid'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[CanManageInvoices])
    def associate_with_customer_or_project(self, request):
        """
        Associates invoices with customers or projects.
        """
        invoice_ids = request.data.get('invoice_ids')
        customer_id = request.data.get('customer_id')

        invoices = Invoice.objects.filter(id__in=invoice_ids)
        if customer_id:
            customer = get_object_or_404(Customer, id=customer_id)
            invoices.update(customer=customer)
        return Response({'status': 'Invoices updated successfully'}, status=status.HTTP_200_OK)


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving, updating,
    and deleting invoice items.
    """
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated, CanManageInvoices]
