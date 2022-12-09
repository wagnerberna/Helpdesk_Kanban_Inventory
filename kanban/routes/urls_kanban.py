from django.urls import path
from kanban.views.kanban import (
    kanban_board,
    kanban_list,
    kanban_task_view_create,
    manager_view,
)

urlpatterns = [
    path("kanban_manager/", manager_view, name="kanban_manager"),
    path("kanban_list/", kanban_list, name="kanban_list"),
    path("kanban_board/<int:id>/", kanban_board, name="kanban_board"),
    path("kanban_task_add/<int:id>/", kanban_task_view_create, name="kanban_task_add"),
]
