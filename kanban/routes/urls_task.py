from django.urls import path
from kanban.views.kanban import manager_view
from kanban.views.task import task_view_create

urlpatterns = [
    path("task_add/", task_view_create, name="task_add"),
    path("task_open/", manager_view, name="task_open_filter"),
    path("task_done/", manager_view, name="task_done_filter"),
]
