from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from helpdesk.api.serializers import DemandFilterSerializer
from helpdesk.api.viewsets import (
    DemandFilterViewSet,
    DemandViewSet,
    StatusViewSet,
    UserViewSet,
)
from helpdesk.forms import SupportFormUpdate, SupportFormUpdateView
from helpdesk.models import Demand

demand_view_set = DemandViewSet()
demand_filter_view_set = DemandFilterViewSet()
user_view_set = UserViewSet()
status_view_set = StatusViewSet()

# pesquisa busca pelo name e se não encontrar passa None
@login_required
def support_view_list_all(request):
    try:
        demands = demand_view_set.get_all(request)
        demand_filter = DemandFilterSerializer(request.GET, queryset=demands)

        print(demand_filter)
        context = {"all_demands": demands, "demand_filter": demand_filter}

        return render(
            request,
            "helpdesk/pages/support_list_demand.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def support_view_list_by_technical(request):
    try:
        user_id = request.user.pk

        # print("REQUEST::::", user_id, user_name)

        all_demands = demand_view_set.get_by_support(user_id)
        # print(all_demands)

        context = {"all_demands": all_demands}

        return render(
            request,
            "helpdesk/pages/support_list_demand.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


# passa uma instância
# readonly ou disable in text form
@login_required
def support_view_update(request, id):
    try:
        # print("ID:::", id)
        demand = demand_view_set.get_by_id(id)
        # demand = get_object_or_404(Demand, pk=id)
        # print(demand)
        form_view = SupportFormUpdateView(request.POST or None, instance=demand)
        form = SupportFormUpdate(request.POST or None, instance=demand)

        form_view.fields["user_name"].widget.attrs["disabled"] = True
        form_view.fields["category"].widget.attrs["disabled"] = True
        form_view.fields["title"].widget.attrs["disabled"] = True
        form_view.fields["description"].widget.attrs["disabled"] = True

        # template =
        context = {"form": form, "form_view": form_view}

        if form.is_valid():
            form.save()
            return redirect("support_list_all")

        return render(request, "helpdesk/pages/support_update_demand.html", context)
    except Exception as error:
        print("Internal error:", error)
        raise
