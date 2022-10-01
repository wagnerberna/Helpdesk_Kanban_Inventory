from django.urls import path
from helpdesk.views.support import (
    support_view_list_all,
    support_view_list_by_technical,
    support_view_update,
)

urlpatterns = [
    path("support/<int:id>/", support_view_update, name="support_update"),
    path("support/", support_view_list_all, name="support_list_all"),
    path(
        "support_technical/",
        support_view_list_by_technical,
        name="support_by_technical",
    ),
]
