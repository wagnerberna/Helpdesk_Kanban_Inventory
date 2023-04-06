from django.urls import path
from inventory.api.viewsets import InventoryViewSets

urlpatterns = [
    path(
        "inventory_api_workstation/",
        InventoryViewSets,
        name="inventory_api_workstation",
    ),
]
