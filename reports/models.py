from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Report(models.Model):
    """
    Model representing a report.
    """
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ReportEntry(models.Model):
    """
    Model representing an entry in a report.
    """
    report = models.ForeignKey(Report, related_name='entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=191)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ReportFile(models.Model):
    """
    Model representing a file attached to a report entry.
    """
    entry = models.ForeignKey(ReportEntry, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='report_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
