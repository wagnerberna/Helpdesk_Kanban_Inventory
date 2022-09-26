from django.urls import path

from helpdesk.views.demand import demand, demand_delete, demand_update, new_demand
from helpdesk.views.home import about, home

# name apelido da URL para referenciar:
#  no action do form / no redirect da view
urlpatterns = [
    path("", home),
    path("demand/", demand, name="demands_list"),
    path("new_demand/", new_demand, name="new_demand"),
    path("demand/<int:id>/", demand_update, name="demand_update"),
    path("delete/<int:id>/", demand_delete, name="demand_delete"),
    path("about/", about),
]
