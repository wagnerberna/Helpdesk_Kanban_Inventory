import datetime
import urllib

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access
from ti.service.dataframe import dataframe_desktop_ranking, open_excel_dataframe
from ti.service.format_time import format_time_delta
from ti.service.make_graphics import (
    make_graphic_bar,
    make_graphic_barh,
    make_graphic_pie,
)


@login_required
def report_per_technical(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # demands_all = Demand.objects.filter(status__name="Finalizado")
        # SLA
        demands_all = Demand.objects.filter(status__name="Finalizado").values(
            "created_at", "updated_at"
        )

        demands_count = demands_all.count()
        # print("demands_all:::", demands_all, demands_count)

        demands_sum = datetime.timedelta(days=0, minutes=0, seconds=0)
        sla_average = datetime.timedelta(days=0, minutes=0, seconds=0)

        # print("demands_sum timedelta:::", demands_sum)
        for el in demands_all:
            created_at = el.get("created_at")
            updated_at = el.get("updated_at")
            difference_between_days = updated_at - created_at
            # convert = difference_between_days
            demands_sum += difference_between_days

            # print("difference_between_days", difference_between_days)
            # print("convert::", convert)
            print("demands_sum", demands_sum)

        if sla_average:
            sla_average = demands_sum / demands_count
            sla_format = format_time_delta(sla_average)
        else:
            sla_format = ""

        # print("SLA:::", sla_average)
        # print("sla_format:::", sla_format)

        # Gráfico Demandas
        demmands_leonardo = Demand.objects.filter(attendant__user_name=4).count()
        demmands_wagner = Demand.objects.filter(attendant__user_name=2).count()

        techinicals_labels = ["Leonardo.susin", "Wagner.berna"]
        demands_total_per_techinical = [demmands_leonardo, demmands_wagner]
        title = "Chamados por Técnico"
        color = "blue"

        graphic_demands = make_graphic_bar(
            title, color, techinicals_labels, demands_total_per_techinical
        )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(task_owner__user_name=4).count()
        tasks_wagner = Task.objects.filter(task_owner__user_name=2).count()

        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]
        title = "Projetos: Tarefas por Técnico"
        color = "red"

        graphic_projects = make_graphic_bar(
            title, color, techinicals_labels, tasks_total_per_techinical
        )

        context = {
            "graphic_demands": urllib.parse.quote(graphic_demands),
            "graphic_projects": urllib.parse.quote(graphic_projects),
            "demmands_leonardo": demmands_leonardo,
            "demmands_wagner": demmands_wagner,
            "tasks_leonardo": tasks_leonardo,
            "tasks_wagner": tasks_wagner,
            "sla": sla_format,
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

        # Table Projects
        projects_names = list(Project.objects.all().values_list("name"))

        # .exclude(status__name="DONE")
        # all_tasks_per_project = Task.objects.all().values_list(
        #     "project__name", "status__name"
        # )
        # print("projects_names:", projects_names)
        # print("contagem projetos:", len(projects_names))
        # print("all_tasks:", all_tasks_per_project)
        # print("contagem tarefas:", all_tasks_per_project.count())

        projects_list = []
        project_percent_to_graphic = []
        projects_labels = []

        for project in projects_names:
            print(project[0])

            project_tasks_total_count = Task.objects.filter(
                project__name=project[0]
            ).count()
            if not project_tasks_total_count:
                project_tasks_total_count = 1

            project_tasks_done_count = Task.objects.filter(
                project__name=project[0], status__name="DONE"
            ).count()

            project_tasks_active = project_tasks_total_count - project_tasks_done_count

            project_percentage = (
                project_tasks_done_count / project_tasks_total_count
            ) * 100
            projects_list.append(
                {
                    "name": project[0],
                    "task_active": project_tasks_active,
                    "task_done": project_tasks_done_count,
                    "task_total": project_tasks_total_count,
                    "project_percentage": round(project_percentage),
                }
            )

            if project_percentage != 100:
                projects_labels.append(project[0])
                project_percent_to_graphic.append(project_percentage)

        projects_list_sorted = sorted(
            projects_list, key=lambda k: k["project_percentage"]
        )

        # print("PROJECT LIST:::", projects_list)
        # print("projects_list_sorted", projects_list_sorted)

        # Graphic projects
        title = "Projetos Percentual de Conclusão"
        color = "red"

        # print(projects_labels, project_percent_to_graphic)
        graphic_projects = make_graphic_barh(
            title, color, projects_labels, project_percent_to_graphic
        )

        context = {
            "graphic_projects": urllib.parse.quote(graphic_projects),
            "projects": projects_list_sorted,
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


@login_required
def topology(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        template_path = "ti/pages/topology.html"
        return render(request, template_path)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def network_racks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        template_path = "ti/pages/network_racks.html"
        return render(request, template_path)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def servers_list(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        file = "doc/vmware.xlsx"
        data = open_excel_dataframe(file)

        template_path = "ti/pages/report_servers.html"
        context = {"data": data}
        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def workstations_list(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        file = "doc/resume.xlsx"
        data = open_excel_dataframe(file)

        # ranking:
        # title = "Workstations"
        # ranking_labels = ["A-i7", "B-i5", "C-i3", "D-Core", "E-Celeron"]
        # ranking_values = dataframe_desktop_ranking(file)
        # graphic_ranking = make_graphic_pie(ranking_labels, ranking_values)

        template_path = "ti/pages/report_workstations.html"
        context = {"data": data}
        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def workstations_ranking(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        file = "doc/resume.xlsx"
        # ranking:
        # title = "Workstations"
        ranking_labels = ["A-i7", "B-i5", "C-i3", "D-Core", "E-Celeron"]
        ranking_values = dataframe_desktop_ranking(file)
        graphic_ranking = make_graphic_pie(ranking_labels, ranking_values)

        template_path = "ti/pages/ranking_workstations.html"
        context = {"graphic_ranking": urllib.parse.quote(graphic_ranking)}
        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise
