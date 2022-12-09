from django.urls import path
from kanban.views.kanban import (
    kanban_board,
    kanban_list,
    kanban_task_view_create,
    kanban_task_view_delete,
    kanban_task_view_update,
    manager_view,
)

urlpatterns = [
    path("kanban_manager/", manager_view, name="kanban_manager"),
    path("kanban_list/", kanban_list, name="kanban_list"),
    path("kanban_board/<int:id>/", kanban_board, name="kanban_board"),
    path(
        "kanban_task_add/<int:id_project>/",
        kanban_task_view_create,
        name="kanban_task_add",
    ),
    path(
        "kanban_task_update/<int:id>/",
        kanban_task_view_update,
        name="kanban_task_update",
    ),
    path(
        "kanban_task_delete/<int:id>/",
        kanban_task_view_delete,
        name="kanban_task_delete",
    ),
]
