from django.urls import path
from inventory.views.inventory import inventory_view_list_all

urlpatterns = [
    path("inventory_list_all/", inventory_view_list_all, name="inventory_list_all"),
    # path("demand_details/<int:id>/", demand_view_details, name="demand_details"),
    # path("new_demand/", demand_view_create, name="new_demand"),
    # path("delete/<int:id>/", demand_view_delete, name="demand_delete"),
    # path("demand_done/", demand_view_list_done, name="demand_list_done"),
]
