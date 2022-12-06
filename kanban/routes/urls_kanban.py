from django.urls import path
from kanban.views.kanban import manager_view

urlpatterns = [
    path("manager/", manager_view, name="kanban_manager"),
    path("board/", manager_view, name="kanban_board"),
]
