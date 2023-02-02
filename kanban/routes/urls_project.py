from django.urls import path
from kanban.views.project import (
    project_view_create,
    project_view_delete,
    project_view_done,
    project_view_open,
    project_view_update,
)

urlpatterns = [
    path(
        "projects_open/",
        project_view_open,
        name="projects_open",
    ),
    path("projects_done/", project_view_done, name="projects_done"),
    path(
        "project_update/<int:id>/",
        project_view_update,
        name="project_update",
    ),
    path(
        "project_delete/<int:id>/",
        project_view_delete,
        name="project_delete",
    ),
    path("project_add/", project_view_create, name="project_add"),
]
