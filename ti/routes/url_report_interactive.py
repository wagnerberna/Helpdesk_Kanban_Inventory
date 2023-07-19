from django.urls import path
from ti.views.report_interactive import report_interactive, report_ocs

urlpatterns = [
    path("dashboard/", report_interactive, name="dashboard"),
]
urlpatterns = [
    path("dashboard_ocs/", report_interactive, name="dashboard_ocs"),
]