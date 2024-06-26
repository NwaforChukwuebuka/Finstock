from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, ReportEntryViewSet, ReportFileViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'report-entries', ReportEntryViewSet)
router.register(r'report-files', ReportFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
