from django.urls import path
from ti.views.report_api import (
    return_total_project_tasks,
    return_total_technicals_demand,
    return_total_technicals_tasks,
    return_total_workstations_ranking,
)

urlpatterns = [
    path(
        "return_total_techicals_demand/",
        return_total_technicals_demand,
        name="return_total_techicals_demand",
    ),
    path(
        "return_total_technicals_tasks/",
        return_total_technicals_tasks,
        name="return_total_technicals_tasks",
    ),
    path(
        "return_total_workstations_ranking/",
        return_total_workstations_ranking,
        name="return_total_workstations_ranking",
    ),
    path(
        "return_total_project_tasks/",
        return_total_project_tasks,
        name="return_total_project_tasks",
    ),
]