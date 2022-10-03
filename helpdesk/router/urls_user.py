from django.urls import path
from helpdesk.views.demand import (
    demand_view_create,
    demand_view_delete,
    demand_view_details,
    demand_view_list_by_user,
)

# from helpdesk.views.home import home

# name apelido da URL para referenciar:
#  no action do form / no redirect da view
urlpatterns = [
    # path("", home),
    path("demand/", demand_view_list_by_user, name="demands_list_by_user"),
    path("demand_details/<int:id>/", demand_view_details, name="demand_details"),
    # path("demand_user/", demand_list_by_user, name="demands_user"),
    path("new_demand/", demand_view_create, name="new_demand"),
    # path("demand/<int:id>/", demand_view_update, name="demand_update"),
    path("delete/<int:id>/", demand_view_delete, name="demand_delete"),
    # path("support/", demand_view_list_all, name="demands_list_all"),
    # path("support_technical/", demand_view_list_support, name="support_technical"),
]
