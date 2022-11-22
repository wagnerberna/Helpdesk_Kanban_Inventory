from django.urls import path
from ti.views.report import report_per_project, report_per_technical

urlpatterns = [
    path("report_per_technical/", report_per_technical, name="report_per_technical"),
    path("report_per_project/", report_per_project, name="report_per_project"),
]
