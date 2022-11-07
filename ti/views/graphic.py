import base64
import io
import urllib

import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.serializers import SupportFilterSerializer
from helpdesk.forms import SupportFormUpdate, SupportFormUpdateView
from helpdesk.models import Demand
from helpdesk.service.check_user_access import check_user_access
from kanban.models import Task


def make_graphic_bar(title, techinicals, total_per_techinical):
    plt.bar(techinicals, total_per_techinical, color="blue")

    plt.title(title)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    return string


@login_required
def graphics(request):
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

        graphic_demands = make_graphic_bar(
            title, techinicals, demands_total_per_techinical
        )

        # Gráfico Projetos
        tasks_leonardo = Task.objects.filter(task_owner__user_name=4).count()
        tasks_wagner = Task.objects.filter(task_owner__user_name=2).count()

        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]
        title = "Projetos: Tarefas por Técnico"

        graphic_projects = make_graphic_bar(
            title, techinicals, tasks_total_per_techinical
        )

        context = {
            "graphic_demands": urllib.parse.quote(graphic_demands),
            "graphic_projects": urllib.parse.quote(graphic_projects),
        }

        # return render(request,'home.html',{'data':uri})

        #     demands = Demand.objects.filter(status__name="Finalizado").order_by("-id")
        #     demand_filter = SupportFilterSerializer(request.GET, queryset=demands)

        #     # print(demand_filter)
        #     context = {"all_demands": demands, "demand_filter": demand_filter}
        template_path = "ti/pages/graphic.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise
