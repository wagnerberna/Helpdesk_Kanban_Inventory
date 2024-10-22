import datetime
import urllib
from multiprocessing import Process

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from django.db.models import Count
from django.shortcuts import redirect, render
from helpdesk.models import Demand
from kanban.models import Project, Task

# from ti.models import Department, Profile
from ti.service.check_user_access import check_user_access
from ti.service.dataframe import (
    dataframe_desktop_ranking,
    excel_to_dataframe,
    excel_to_json,
)
from ti.service.format_time import format_time_delta
from ti.service.make_graphics import MakeGraphics
from ti.service.resume_hardware import ProcessHardwareFiles

make_graphics = MakeGraphics()
convert_files = ProcessHardwareFiles()


@login_required
def report_per_technical(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # SLA
        demands_all = Demand.objects.filter(status__name="Concluído").values(
            "created_at", "updated_at"
        )
        demands_count = demands_all.count()

        # SLA
        demands_sum = datetime.timedelta(days=0, minutes=0, seconds=0)
        sla_average = datetime.timedelta(days=0, minutes=0, seconds=0)

        for el in demands_all:
            created_at = el.get("created_at")
            updated_at = el.get("updated_at")
            difference_between_days = updated_at - created_at
            demands_sum += difference_between_days

        # if sla_average:
        sla_average = demands_sum / demands_count
        sla_format = format_time_delta(sla_average)
        # else:
        # sla_format = ""

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
        demands_total_per_techinical = [demmands_leonardo, demmands_wagner]
        title = "Chamados por Técnico"
        color = "#7fe686"

        graphic_demands = make_graphics.bar(
            title, color, techinicals_labels, demands_total_per_techinical
        )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(
            task_owner__user_name=techinical_leonardo_id
        ).count()
        tasks_wagner = Task.objects.filter(
            task_owner__user_name=techinical_Wagner_id
        ).count()

        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]
        title = "Projetos: Tarefas por Técnico"
        color = "#86cbf9"

        graphic_projects = make_graphics.bar(
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

        projects_list = []
        project_percent_to_graphic = []
        projects_labels = []

        for project in projects_names:

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

        # ordenar os valores da lista pela chave do dict
        projects_list_sorted = sorted(
            projects_list, key=lambda k: k["project_percentage"]
        )

        # Graphic projects percent DONE
        title = "Projetos: Percentual de Conclusão"
        color = "#86cbf9"

        graphic_projects = make_graphics.barh(
            title, color, projects_labels, project_percent_to_graphic
        )

        # graphics projects per task's status
        df_projects_tasks_status = pd.DataFrame(
            Task.objects.all()
            .exclude(project__status__name="DONE")
            .values("id", "project__name", "status__name")
        )
        # print(df_projects_tasks_status)

        ylabel = "Quantidade"
        xlabel = "Projetos"
        title = "Projetos: Quantidade e Status das Tarefas"
        graphic_projects_tasks_status = make_graphics.bar_project(
            title, xlabel, ylabel, df_projects_tasks_status
        )

        context = {
            "graphic_projects": urllib.parse.quote(graphic_projects),
            "graphic_projects_tasks_status": urllib.parse.quote(
                graphic_projects_tasks_status
            ),
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
        data = excel_to_json(file)

        template_path = "ti/pages/report_servers.html"
        context = {"data": data}
        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def workstations_table_update(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # processo em segundo plano
        start_process = False

        if request.method == "POST":
            process = Process(target=convert_files.process_file, args=())
            process.start()
            start_process = True

        template_path = "ti/pages/update_workstations.html"
        context = {"start_process": start_process}
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
        data = excel_to_json(file)

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
        # print(ranking_values)

        graphic_ranking = make_graphics.pie_ranking(ranking_labels, ranking_values)

        # ranking sector:
        departments_adm = [
            "Comercial",
            "Engenharia",
            "Direcao",
            "Controladoria",
            "Fiscal",
            "Contabilidade",
            "Financeiro",
            "TI",
            "RH",
            "Marketing",
            "Juridico",
            "Zeladoria",
            "SESMT",
            "Qualidade",
        ]
        departments_fab = [
            "Ferramentaria",
            "Fundidos",
            "Almoxarifado",
            "Compras",
            "Lideres",
            "PCP",
            "Bobinagem",
            "Expedicao",
            "Industrial",
            "Montagem",
            "Manutencao",
        ]

        df = excel_to_dataframe(file)
        df_adm = df.loc[df["Setor"].isin(departments_adm)]
        df_fab = df.loc[df["Setor"].isin(departments_fab)]

        ylabel = "Quantidade"
        xlabel = "Setores"
        title_adm = "Administrativo Quantidade de Estações por Categoria"
        title_fab = "Fabrica Quantidade de Estações por Categoria"
        graphic_departaments_adm = make_graphics.bar_ranking(
            title_adm, xlabel, ylabel, df_adm
        )
        graphic_departaments_fab = make_graphics.bar_ranking(
            title_fab, xlabel, ylabel, df_fab
        )

        template_path = "ti/pages/ranking_workstations.html"
        context = {
            "graphic_ranking": urllib.parse.quote(graphic_ranking),
            "graphic_departaments_adm": urllib.parse.quote(graphic_departaments_adm),
            "graphic_departaments_fab": urllib.parse.quote(graphic_departaments_fab),
        }
        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise
