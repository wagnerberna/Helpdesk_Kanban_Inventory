from django.urls import path
from ti.views.report import (
    report_per_project,
    report_per_technical,
    servers_list,
    topology,
    workstations_list,
    workstations_ranking,
)

urlpatterns = [
    path("report_per_technical/", report_per_technical, name="report_per_technical"),
    path("report_per_project/", report_per_project, name="report_per_project"),
    path("topology/", topology, name="topology"),
    path("servers/", servers_list, name="servers"),
    path("workstations/", workstations_list, name="workstations"),
    path("ranking/", workstations_ranking, name="ranking"),
]
