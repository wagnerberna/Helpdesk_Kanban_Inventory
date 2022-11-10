import urllib

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from helpdesk.service.check_user_access import check_user_access
from kanban.models import Task
from ti.service.make_graphics import make_graphic_bar


@login_required
def graphics_per_technical(request):
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

        # Gráfico Projetos
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
        }

        template_path = "ti/pages/graphic.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise
