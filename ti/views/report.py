import urllib

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access
from ti.service.make_graphics import make_graphic_bar


@login_required
def report_per_technical(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # Gráfico Demandas
        demmands_leonardo = Demand.objects.filter(attendant__user_name=4).count()
        demmands_wagner = Demand.objects.filter(attendant__user_name=2).count()

        techinicals = ["Leonardo.susin", "Wagner.berna"]
        demands_total_per_techinical = [demmands_leonardo, demmands_wagner]
        title = "Chamados por Técnico"
        color = "blue"

        graphic_demands = make_graphic_bar(
            title, color, techinicals, demands_total_per_techinical
        )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(task_owner__user_name=4).count()
        tasks_wagner = Task.objects.filter(task_owner__user_name=2).count()

        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]
        title = "Projetos: Tarefas por Técnico"
        color = "red"

        graphic_projects = make_graphic_bar(
            title, color, techinicals, tasks_total_per_techinical
        )

        context = {
            "graphic_demands": urllib.parse.quote(graphic_demands),
            "graphic_projects": urllib.parse.quote(graphic_projects),
            "demmands_leonardo": demmands_leonardo,
            "demmands_wagner": demmands_wagner,
            "tasks_leonardo": tasks_leonardo,
            "tasks_wagner": tasks_wagner,
        }

        template_path = "ti/pages/report_per_technical.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def report_per_project(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # Gráfico Projeto
        projects_names = list(Project.objects.all().values_list("name"))
        all_tasks_per_project = Task.objects.all().values_list(
            "project__name", "status__name"
        )
        print("projects_names:", projects_names)
        print("contagem projetos:", len(projects_names))
        print("all_tasks:", all_tasks_per_project)
        # print("contagem tarefas:", all_tasks_per_project.count())

        project_tasks_total_count = Task.objects.filter(
            project__name="Migração Servidor Impressão"
        ).count()
        project_tasks_done_count = Task.objects.filter(
            project__name="Migração Servidor Impressão", status__name="DONE"
        ).count()
        project_tasks_active = project_tasks_total_count - project_tasks_done_count

        print("project_tasks_count total migração:::", project_tasks_total_count)
        print("project_tasks_count migração Done:::", project_tasks_done_count)
        print("project_tasks_count migração active:::", project_tasks_active)

        projects_list = []

        for project in projects_names:
            print(project[0])

            project_tasks_total_count = Task.objects.filter(
                project__name=project[0]
            ).count()
            project_tasks_done_count = Task.objects.filter(
                project__name=project[0], status__name="DONE"
            ).count()
            project_tasks_active = project_tasks_total_count - project_tasks_done_count
            project_percentage = (
                project_tasks_done_count / project_tasks_total_count
            ) * 100
            projects_list.append(
                # [
                {
                    "name": project[0],
                    "task_active": project_tasks_active,
                    "task_done": project_tasks_done_count,
                    "task_total": project_tasks_total_count,
                    "project_percentage": project_percentage,
                }
                # ]
            )

        print(projects_list)

        for el in projects_list:
            print(el["name"])

        techinicals = ["Leonardo.susin", "Wagner.berna"]
        demands_total_per_techinical = ["demmands_leonardo", "demmands_wagner"]
        title = "Chamados por Técnico"
        color = "blue"

        # graphic_demands = make_graphic_bar(
        #     title, color, techinicals, demands_total_per_techinical
        # )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(task_owner__user_name=4).count()
        tasks_wagner = Task.objects.filter(task_owner__user_name=2).count()

        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]
        title = "Projetos: Tarefas por Técnico"
        color = "red"

        # graphic_projects = make_graphic_bar(
        #     title, color, techinicals, tasks_total_per_techinical
        # )

        context = {
            # "graphic_demands": urllib.parse.quote(graphic_demands),
            # "graphic_projects": urllib.parse.quote(graphic_projects),
            "projects": projects_list,
        }

        template_path = "ti/pages/report_per_project.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise
