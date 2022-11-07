from django.urls import path
from kanban.views.kanban import manager_view
from kanban.views.task import (
    task_view_create,
    task_view_done,
    task_view_open,
    task_view_update,
)

urlpatterns = [
    path("task_add/", task_view_create, name="task_add"),
    path("task_open/", task_view_open, name="task_open_filter"),
    path("task_done/", task_view_done, name="task_done_filter"),
    path(
        "task_update/<int:id>/",
        task_view_update,
        name="task_update",
    ),
    path(
        "task_delete/<int:id>/",
        task_view_update,
        name="task_delete",
    ),
]
