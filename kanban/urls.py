from django.urls import path

from kanban.views.kanban import manager_view

urlpatterns = [
    path("manager/", manager_view, name="kanban_manager"),
    path("list_projects_open/", manager_view, name="kanban_list_projects_open"),
    path("list_projects_done/", manager_view, name="kanban_list_projects_done"),
    path("add_project/", manager_view, name="kanban_add_project"),
    path("list_category/", manager_view, name="kanban_list_category"),
    path("add_category/", manager_view, name="kanban_add_category"),
    path("add_task/", manager_view, name="kanban_add_task"),
]
