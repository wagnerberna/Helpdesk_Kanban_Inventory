from django.urls import path
from ti.views.report_interactive import report_interactive

urlpatterns = [
    path("new/", report_interactive, name="new"),
]
