from django.urls import path
from inventory.views.inventory import inventory_view_workstation, inventory_view_server

urlpatterns = [
    path("inventory_workstation/", inventory_view_workstation, name="inventory_workstation"),
    path("inventory_server/", inventory_view_server, name="inventory_server"),
]
