from django.urls import path

from kanban.views.site import about, home

urlpatterns = [
    path("", home),
    path("about/", about),
]
