# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

# from kanban.api.serializers import KanbanFilterSerializer
# from kanban.forms import
# from kanban.models import Kanban


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Support.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True


@login_required
def manager(request):
    return render(
        request,
        "kanban/pages/kanban_manager.html",
        context={"title": "Kanban"},
    )
