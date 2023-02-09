# from django import forms
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from ti.service.check_user_access import check_user_access

from kanban.forms import KanbanStatusFormNext, TaskForm
from kanban.models import Category, Project, Status, Task, Team

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
def kanban_projects(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects_doing = (
            Project.objects.all().order_by("id").exclude(status__name="DONE")
        )
        projects_done = Project.objects.filter(status__name="DONE").order_by("id")

        context = {"projects_doing": projects_doing, "projects_done": projects_done}
        template_path = "kanban/pages/kanban_projects.html"

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

        form = KanbanStatusFormNext(request.POST)
        context = {
            "project_name": project_name,
            "project_id": id,
            "tasks": tasks,
            "form": form,
        }
        template_path = "kanban/pages/kanban_board.html"

        # click for move task
        if request.method == "POST":
            req = request.POST
            id_task = req.get("id_task")
            print(id_task)
            task_status_id = (
                Task.objects.filter(pk=id_task).values("status")[0].get("status")
            )

            if task_status_id == 1:
                Task.objects.filter(pk=id_task).update(status=2)
            elif task_status_id == 2:
                Task.objects.filter(pk=id_task).update(status=3)
            elif task_status_id == 3:
                Task.objects.filter(pk=id_task).update(status=4)
            elif task_status_id == 4:
                Task.objects.filter(pk=id_task).update(status=1)

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_task_view_create(request, id_project):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        form = TaskForm(request.POST or None)
        form.fields["project"].initial = id_project
        form.fields["status"].initial = 1
        # form.fields["user_name"].widget = forms.HiddenInput()

        context = {"form": form}
        template_path = "kanban/pages/task_create.html"

        if form.is_valid():
            form.save()
            return redirect("kanban_board", id=id_project)

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_task_view_delete(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        task = get_object_or_404(Task, pk=id)
        project_id = task.project.id

        context = {"project": task}
        template_path = "kanban/pages/task_delete.html"

        if request.method == "POST":
            task.delete()
            return redirect("kanban_board", id=project_id)

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def kanban_task_view_update(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        task = get_object_or_404(Task, pk=id)
        project_id = task.project.id

        form = TaskForm(request.POST or None, instance=task)

        context = {"form": form}
        template_path = "kanban/pages/task_update.html"

        if form.is_valid():
            form.save()
            return redirect("kanban_board", id=project_id)

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
