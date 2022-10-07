from django.urls import path
from helpdesk.views.demand import (
    demand_view_create,
    demand_view_delete,
    demand_view_details,
    demand_view_list_by_user,
    demand_view_list_done,
)

# from helpdesk.views.home import home

# name apelido da URL para referenciar:
#  no action do form / no redirect da view
urlpatterns = [
    path("demand/", demand_view_list_by_user, name="demands_list_by_user"),
    path("demand_details/<int:id>/", demand_view_details, name="demand_details"),
    path("new_demand/", demand_view_create, name="new_demand"),
    path("delete/<int:id>/", demand_view_delete, name="demand_delete"),
    path("demand_done/", demand_view_list_done, name="demand_list_done"),
]
