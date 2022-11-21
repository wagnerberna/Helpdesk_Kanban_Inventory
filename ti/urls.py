from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

from ti.views.home import (
    ChangePassword,
    about,
    access_denied,
    home,
    login_user,
    logout_user,
)
from ti.views.report import report_per_project, report_per_technical

# Importar views do Django de autenticação
# criar Urls de login e logout

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("login/", views.LoginView.as_view(), name="login"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("changepassword/", ChangePassword, name="changepassword"),
    path("access_denied/", access_denied, name="access_denied"),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("helpdesk/", include("helpdesk.routes.urls_user")),
    path("helpdesk/", include("helpdesk.routes.urls_support")),
    path("kanban/", include("kanban.routes.urls_kanban")),
    path("kanban/", include("kanban.routes.urls_project")),
    path("kanban/", include("kanban.routes.urls_task")),
    # path("kanban/api/", include("kanban.api.urls")),
    # path("helpdesk/api/", include("helpdesk.api.urls")),
    path("report_per_technical/", report_per_technical, name="report_per_technical"),
    path("report_per_project/", report_per_project, name="report_per_project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
