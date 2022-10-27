from django.urls import path

from kanban.views.kanban import (
    kanban_view_projects_done,
    kanban_view_projects_open,
    manager_view,
    project_view_create,
)

urlpatterns = [
    path("manager/", manager_view, name="kanban_manager"),
    path(
        "projects_open/",
        kanban_view_projects_open,
        name="kanban_projects_open",
    ),
    path("projects_done/", kanban_view_projects_done, name="kanban_projects_done"),
    path("add_project/", project_view_create, name="kanban_add_project"),
    # path("list_category/", manager_view, name="kanban_list_category"),
    # path("add_category/", manager_view, name="kanban_add_category"),
    path("add_task/", manager_view, name="kanban_add_task"),
]
