import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access
from ti.service.dataframe import dataframe_desktop_ranking
from inventory.models import Inventory


@login_required
def api_total_technicals_demand(request):
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

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def api_total_technicals_tasks(request):
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
def api_total_project_tasks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # Table Projects
        projects_names = list(Project.objects.all().values_list("name"))

        projects_labels = []
        tasks_to_do = []
        tasks_doing = []
        tasks_blocked = []
        tasks_done = []
        tasks_active = []
        tasks_done = []
        tasks_total = []
        project_percentage = []
        label_status = ["TO DO", "DOING", "BLOCKED", "DONE"]

        for project in projects_names:

            tasks_total_count = Task.objects.filter(project__name=project[0]).count()
            if not tasks_total_count:
                tasks_total_count = 1

            tasks_to_do_count = Task.objects.filter(
                project__name=project[0], status__name="TO DO"
            ).count()

            tasks_doing_count = Task.objects.filter(
                project__name=project[0], status__name="DOING"
            ).count()

            tasks_blocked_count = Task.objects.filter(
                project__name=project[0], status__name="BLOCKED"
            ).count()

            tasks_done_count = Task.objects.filter(
                project__name=project[0], status__name="DONE"
            ).count()

            tasks_active_count = tasks_total_count - tasks_done_count

            percentage = round((tasks_done_count / tasks_total_count) * 100)

            if percentage != 100:
                projects_labels.append(project[0])
                tasks_total.append(tasks_total_count)
                tasks_active.append(tasks_active_count)
                tasks_to_do.append(tasks_to_do_count)
                tasks_doing.append(tasks_doing_count)
                tasks_blocked.append(tasks_blocked_count)
                tasks_done.append(tasks_done_count)
                project_percentage.append(percentage)

        context = {
            "labels": projects_labels,
            "label_status": label_status,
            "tasks_total": tasks_total,
            "tasks_active": tasks_active,
            "tasks_to_do": tasks_to_do,
            "tasks_doing": tasks_doing,
            "tasks_blocked": tasks_blocked,
            "tasks_done": tasks_done,
            "project_percentage": project_percentage,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def api_total_workstations_ranking(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        ranking_a = Inventory.objects.filter(ranking__name="A").count()
        ranking_b = Inventory.objects.filter(ranking__name="B").count()
        ranking_c = Inventory.objects.filter(ranking__name="C").count()
        ranking_d = Inventory.objects.filter(ranking__name="D").count()
        ranking_e = Inventory.objects.filter(ranking__name="E").count()

        ranking_workstation = [ranking_a, ranking_b, ranking_c, ranking_d, ranking_e]
        ranking_labels = ["A-i7", "B-i5", "C-i3", "D-Core", "E-Celeron"]

        context = {
            "data": ranking_workstation,
            "labels": ranking_labels,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise
