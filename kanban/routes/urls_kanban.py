from django.urls import path
from kanban.views.kanban import kanban_board, manager_view

urlpatterns = [
    path("manager/", manager_view, name="kanban_manager"),
    path("board/", kanban_board, name="kanban_board"),
]
