from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.viewsets import DemandViewSet
from helpdesk.forms import DemandFormCreate, DemandFormUpdate
from helpdesk.models import Demand

demand_view_set = DemandViewSet()


@login_required
def demand_list_support(request):
    try:
        all_demands = demand_view_set.get_all(request)
        # print(all_demands)

        context = {"title": "Demandas", "all_demands": all_demands}

        return render(
            request,
            "helpdesk/pages/demand_list_all.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise
