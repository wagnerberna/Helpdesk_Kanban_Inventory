from django.urls import path
from helpdesk.views.support import (
    support_view_list_by_technical,
    support_view_list_done,
    support_view_list_open,
    support_view_update,
)
from helpdesk.views.support_report import report_by_techinical

urlpatterns = [
    path("support/<int:id>/", support_view_update, name="support_update"),
    path("support/", support_view_list_open, name="support_list_all"),
    path(
        "support_technical/",
        support_view_list_by_technical,
        name="support_by_technical",
    ),
    path("support_done/", support_view_list_done, name="support_list_done"),
    path("report_by_techinical/", report_by_techinical, name="report_by_techinical"),
]
