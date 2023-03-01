from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access
from ti.service.dataframe import dataframe_desktop_ranking


@login_required
def return_total_technicals_demand(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        techinical_Wagner_id = (
            User.objects.filter(username="wagner.berna").values("id")[0].get("id")
        )
        techinical_leonardo_id = (
            User.objects.filter(username="leonardo.susin").values("id")[0].get("id")
        )

        # Gráfico Demandas
        demmands_leonardo = Demand.objects.filter(
            attendant__user_name=techinical_leonardo_id
        ).count()
        demmands_wagner = Demand.objects.filter(
            attendant__user_name=techinical_Wagner_id
        ).count()

        techinicals_labels = ["Leonardo.susin", "Wagner.berna"]
        demands_total_per_technical = [demmands_leonardo, demmands_wagner]

        context = {
            "data": demands_total_per_technical,
            "labels": techinicals_labels,
        }
        # print(context)

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def return_total_technicals_tasks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        techinical_Wagner_id = (
            User.objects.filter(username="wagner.berna").values("id")[0].get("id")
        )
        techinical_leonardo_id = (
            User.objects.filter(username="leonardo.susin").values("id")[0].get("id")
        )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(
            task_owner__user_name=techinical_leonardo_id
        ).count()
        tasks_wagner = Task.objects.filter(
            task_owner__user_name=techinical_Wagner_id
        ).count()

        techinicals_labels = ["Leonardo.susin", "Wagner.berna"]
        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]

        context = {"data": tasks_total_per_techinical, "labels": techinicals_labels}
        # print(context)

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def return_total_project_tasks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # Table Projects
        projects_names = list(Project.objects.all().values_list("name"))

        projects_labels = []
        project_tasks_active = []
        project_tasks_done = []
        project_tasks_total = []
        project_percentage = []

        for project in projects_names:

            project_tasks_total_count = Task.objects.filter(
                project__name=project[0]
            ).count()
            if not project_tasks_total_count:
                project_tasks_total_count = 1

            project_tasks_done_count = Task.objects.filter(
                project__name=project[0], status__name="DONE"
            ).count()
            # if not project_tasks_done_count:
            #     project_tasks_done_count = 0

            tasks_active_count = project_tasks_total_count - project_tasks_done_count

            percentage = round(
                (project_tasks_done_count / project_tasks_total_count) * 100
            )

            if percentage != 100:
                projects_labels.append(project[0])
                project_tasks_total.append(project_tasks_total_count)
                project_tasks_active.append(tasks_active_count)
                project_tasks_done.append(project_tasks_done_count)
                project_percentage.append(percentage)

            print(project_tasks_done)
        context = {
            "labels": projects_labels,
            "tasks_total": project_tasks_total,
            "tasks_active": project_tasks_active,
            "tasks_done": project_tasks_done,
            "project_percentage": project_percentage,
        }
        print(context)

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def return_total_workstations_ranking(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        file = "doc/resume.xlsx"
        # ranking:
        # title = "Workstations"
        ranking_labels = ["A-i7", "B-i5", "C-i3", "D-Core", "E-Celeron"]
        ranking_values = dataframe_desktop_ranking(file)

        context = {"data": ranking_values, "labels": ranking_labels}
        # print(context)

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise
