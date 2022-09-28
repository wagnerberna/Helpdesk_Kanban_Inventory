from django.urls import path

from helpdesk.views.demand import (
    demand_delete,
    demand_list_all,
    demand_list_by_user,
    demand_list_support,
    demand_update,
    new_demand,
)
from helpdesk.views.home import about, home

# name apelido da URL para referenciar:
#  no action do form / no redirect da view
urlpatterns = [
    path("", home),
    path("demand/", demand_list_by_user, name="demands_list_by_user"),
    # path("demand_user/", demand_list_by_user, name="demands_user"),
    path("new_demand/", new_demand, name="new_demand"),
    path("demand/<int:id>/", demand_update, name="demand_update"),
    path("delete/<int:id>/", demand_delete, name="demand_delete"),
    path("support/", demand_list_all, name="demands_list_all"),
    path("support_technical/", demand_list_support, name="support_technical"),
    # path("about/", about),
]
