from django.urls import path
from ti.views.report import (
    network_racks,
    report_per_project,
    report_per_technical,
    servers_list,
    topology,
    workstations_list,
    workstations_ranking,
    workstations_table_update,
)
from ti.views.report_interactive import report_interactive

urlpatterns = [
    path("report_per_technical/", report_per_technical, name="report_per_technical"),
    path("report_per_project/", report_per_project, name="report_per_project"),
    # path(
    #     "report_per_departament/", report_per_departament, name="report_per_departament"
    # ),
    path("topology/", topology, name="topology"),
    path("network_racks/", network_racks, name="network_racks"),
    path("servers/", servers_list, name="servers"),
    path("workstations/", workstations_list, name="workstations"),
    path("workstations_update/", workstations_table_update, name="workstations_update"),
    path("ranking/", workstations_ranking, name="ranking"),
    path("new/", report_interactive, name="new"),
]
