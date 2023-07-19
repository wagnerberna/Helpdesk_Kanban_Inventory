from django.urls import path
from ti.views.report_interactive import report_interactive, report_ocs

urlpatterns = [
    path("dashboard/", report_interactive, name="dashboard"),
    path("dashboard_ocs/", report_ocs, name="dashboard_ocs"),
]
