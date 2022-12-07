# from django import forms
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from ti.service.check_user_access import check_user_access

from kanban.forms import KanbanStatusFormNext
from kanban.models import Category, Project, Task, Team

# from kanban.api.serializers import KanbanFilterSerializer
# from kanban.forms import


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
def kanban_list(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects = Project.objects.all().order_by("-id").exclude(status__name="DONE")

        context = {"projects": projects}
        template_path = "kanban/pages/kanban_list.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_board(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        project = Project.objects.filter(id=id).values("name")
        project_name = project.values("name")[0].get("name")

        tasks = Task.objects.filter(project__id=id)

        # print("project:::", project_name)
        form = KanbanStatusFormNext(request.POST)
        context = {"project": project_name, "tasks": tasks, "form": form}
        template_path = "kanban/pages/kanban_board.html"

        if request.method == "POST":
            req = request.POST
            id_task = req.get("id_task")

            print("clicou")

            print(req)
            print(id_task)

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
