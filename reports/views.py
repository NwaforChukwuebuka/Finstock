from rest_framework import viewsets
from .models import Report, ReportEntry, ReportFile
from .serializers import ReportSerializer, ReportEntrySerializer, ReportFileSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing report instances.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportEntryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing report entry instances.
    """
    queryset = ReportEntry.objects.all()
    serializer_class = ReportEntrySerializer


class ReportFileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing report file instances.
    """
    queryset = ReportFile.objects.all()
    serializer_class = ReportFileSerializer
