from django.urls import path
from ti.views.report_return_json import return_total_technicals_demand

urlpatterns = [
    path(
        "return_total_techicals_demand/",
        return_total_technicals_demand,
        name="return_total_techicals_demand",
    ),
]
