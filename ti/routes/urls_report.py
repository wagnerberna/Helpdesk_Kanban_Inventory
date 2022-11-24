from django.urls import path
from ti.views.report import (
    workstations_list,
    report_per_project,
    report_per_technical,
    servers_list,
    topology,
)

urlpatterns = [
    path("report_per_technical/", report_per_technical, name="report_per_technical"),
    path("report_per_project/", report_per_project, name="report_per_project"),
    path("topology/", topology, name="topology"),
    path("servers/", servers_list, name="servers"),
    path("workstations/", workstations_list, name="workstations"),
]
