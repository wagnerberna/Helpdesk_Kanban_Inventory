from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access


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

        context = {"data": demands_total_per_technical, "labels": techinicals_labels}
        print(context)

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
        print(context)

        return JsonResponse(context)
    except Exception as error:
        print("Internal error:", error)
        raise
