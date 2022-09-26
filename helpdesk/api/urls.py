from django.urls import include, path
from helpdesk.api.viewsets import DemandViewSet
from rest_framework import routers

# name apelido da URL para referenciar na action do form
route = routers.DefaultRouter()
route.register(r"demand", DemandViewSet, basename="helpdesk_demand")

urlpatterns = [
    path("", include(route.urls)),
]
