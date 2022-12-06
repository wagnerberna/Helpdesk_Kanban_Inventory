# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access

# from kanban.forms import ProjectForm
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
def kanban_board(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects_names = list(
            Project.objects.all().values_list("name").exclude(status__name="DONE")
        )
        print("projects_names:::", projects_names)
        projects_list = []

        for project in projects_names:
            task_list = []
            project_name = project[0]
            # print(project_name)
            project_tasks_to_do = Task.objects.filter(
                project__name=project_name, status__name="TO DO"
            )
            # title_to_do = project_tasks_to_do.values("title")

            project_tasks_doing = Task.objects.filter(
                project__name=project_name, status__name="DOING"
            )
            project_tasks_done = Task.objects.filter(
                project__name=project_name, status__name="DONE"
            )

            # print("project_tasks_to_do:::", project_tasks_to_do)

            for el in projects_list:
                print(el)

            projects_list.append(
                {
                    "project_name": project_name,
                    "tasks_active": project_tasks_to_do,
                    "tasks_doing": project_tasks_doing,
                    "tasks_done": project_tasks_done,
                }
            )

        print(projects_list)
        context = {"projects_list": projects_list}
        template_path = "kanban/pages/kanban_board.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
