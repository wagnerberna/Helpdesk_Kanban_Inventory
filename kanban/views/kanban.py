# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from kanban.forms import ProjectFormCreate
from kanban.models import Category, Project, Task, Team

# from kanban.api.serializers import KanbanFilterSerializer
# from kanban.forms import


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Team.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True


@login_required
def manager_view(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        template_path = "kanban/pages/kanban_manager.html"

        return render(
            request,
            template_path,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def project_view_create(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        form = ProjectFormCreate(request.POST or None)
        context = {"form": form}
        template_path = "kanban/pages/project_create.html"

        if form.is_valid():
            form.save()
            return redirect("kanban_manager")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_view_projects_open(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects = Project.objects.all().order_by("-id").exclude(status__name="DONE")

        context = {"projects": projects}
        template_path = "kanban/pages/project_list_open.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_view_projects_done(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects = Project.objects.filter(status__name="DONE").order_by("-id")

        context = {"projects": projects}
        template_path = "kanban/pages/project_list_done.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_view_project_update(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        project = get_object_or_404(Project, pk=id)

        form = ProjectFormCreate(request.POST or None, instance=project)

        context = {"form": form}
        template_path = "kanban/pages/project_update.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
