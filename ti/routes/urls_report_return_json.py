from django.urls import path
from ti.views.report_return_json import (
    return_total_technicals_demand,
    return_total_technicals_tasks,
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
]
