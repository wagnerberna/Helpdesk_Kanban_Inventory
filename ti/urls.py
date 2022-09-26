from django import views
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

from ti.views.home import home

# Importar views do Django de autenticação
# criar Urls de login e logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", home),
    # path("about/", about),
    path("helpdesk/", include("helpdesk.urls")),
    path("kanban/", include("kanban.urls")),
    path("kanban/api/", include("kanban.api.urls")),
    path("helpdesk/api/", include("helpdesk.api.urls")),
]
