from django.urls import include, path
from kanban.api.viewsets import ProjectViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"project", ProjectViewSet, basename="kanban_project")

urlpatterns = [
    path("", include(route.urls)),
]
