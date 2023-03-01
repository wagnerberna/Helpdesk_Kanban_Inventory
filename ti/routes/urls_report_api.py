from django.urls import path
from ti.views.report_api import (
    api_total_project_tasks,
    api_total_technicals_demand,
    api_total_technicals_tasks,
    api_total_workstations_ranking,
)

urlpatterns = [
    path(
        "api_total_techicals_demand/",
        api_total_technicals_demand,
        name="api_total_techicals_demand",
    ),
    path(
        "api_total_technicals_tasks/",
        api_total_technicals_tasks,
        name="api_total_technicals_tasks",
    ),
    path(
        "api_total_workstations_ranking/",
        api_total_workstations_ranking,
        name="api_total_workstations_ranking",
    ),
    path(
        "api_total_project_tasks/",
        api_total_project_tasks,
        name="return_total_project_tasks",
    ),
]
