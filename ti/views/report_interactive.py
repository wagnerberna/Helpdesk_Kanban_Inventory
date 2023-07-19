from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access
from helpdesk.models import Demand
from kanban.models import Task
from inventory.models import Inventory
import pandas as pd


@login_required
def report_interactive(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        demands_total = Demand.objects.all().count()
        tasks_total = Task.objects.all().count()
        workstation_total = Inventory.objects.all().count()

        template_path = "ti/pages/report_dashboard.html"

        context = {
            "demands_total": demands_total,
            "tasks_total": tasks_total,
            "workstation_total": workstation_total,
        }

        # print("context:::", context)

        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise

@login_required
def report_ocs(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")
        
        print("Ponto0")
        data = pd.read_json("doc/resume.json")
        print(data)

        template_path = "ti/pages/report_dashboard_ocs.html"

        context = {
            "demands_total": "demands_total",
            "tasks_total": "tasks_total",
            "workstation_total": "workstation_total",
        }

        # print("context:::", context)

        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise

