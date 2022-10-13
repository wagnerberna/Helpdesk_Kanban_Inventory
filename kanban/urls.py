from django.urls import path

from kanban.views.kanban import manager

urlpatterns = [
    path("manager/", manager, name="kanban_manager"),
]
