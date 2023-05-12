from django.urls import path
from ti.views.report_api import (
    api_project_tasks,
    api_technicals_demand,
    api_technicals_tasks,
    api_workstations_ranking,
    api_workstations_department_ranking,
)

urlpatterns = [
    path(
        "api_technicals_demand/",
        api_technicals_demand,
        name="api_technicals_demand",
    ),
    path(
        "api_technicals_tasks/",
        api_technicals_tasks,
        name="api_technicals_tasks",
    ),
    path(
        "api_workstations_ranking/",
        api_workstations_ranking,
        name="api_workstations_ranking",
    ),
    path(
        "api_workstations_department_ranking/",
        api_workstations_department_ranking,
        name="api_workstations_department_ranking",
    ),
    path(
        "api_project_tasks/",
        api_project_tasks,
        name="api_project_tasks",
    ),
]
