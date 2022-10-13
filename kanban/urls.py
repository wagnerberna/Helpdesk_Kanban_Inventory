from django.urls import path

from kanban.views.kanban import manager

urlpatterns = [
    path("manager/", manager, name="kanban_manager"),
    path("list_projects_open/", manager, name="kanban_list_projects_open"),
    path("list_projects_done/", manager, name="kanban_list_projects_done"),
    path("add_project/", manager, name="kanban_add_project"),
    path("list_category/", manager, name="kanban_list_category"),
    path("add_category/", manager, name="kanban_add_category"),
    path("add_task/", manager, name="kanban_add_task"),
]
