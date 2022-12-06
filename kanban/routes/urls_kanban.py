from django.urls import path
from kanban.views.kanban import kanban_board, kanban_list, manager_view

urlpatterns = [
    path("kanban_manager/", manager_view, name="kanban_manager"),
    path("kanban_list/", kanban_list, name="kanban_list"),
    path("kanban_board/<int:id>/", kanban_board, name="kanban_board"),
]
