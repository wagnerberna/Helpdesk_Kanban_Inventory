from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.serializers import SupportFilterSerializer
from helpdesk.forms import HistoricFormAdd, SupportFormUpdate, SupportFormUpdateView
from helpdesk.models import Demand, Historic
from ti.service.check_user_access import check_user_access


@login_required
def support_view_list_open(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        demands = (
            Demand.objects.all().order_by("-id").exclude(status__name="Finalizado")
        )
        demand_filter = SupportFilterSerializer(request.GET, queryset=demands)

        print(demand_filter)
        context = {"all_demands": demands, "demand_filter": demand_filter}
        template_path = "helpdesk/pages/support_list_demands_open.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def support_view_list_done(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        demands = Demand.objects.filter(status__name="Finalizado").order_by("-id")
        demand_filter = SupportFilterSerializer(request.GET, queryset=demands)

        # print(demand_filter)
        context = {"all_demands": demands, "demand_filter": demand_filter}
        template_path = "helpdesk/pages/support_list_demands_done.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


# "__" consulta o campo na tabela estrangeira
@login_required
def support_view_list_by_technical(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        id = request.user.pk
        # user_name = request.user.username

        # print("REQUEST::::", id)

        demands = Demand.objects.filter(attendant__user_name=id)
        print(demands)

        context = {"demands": demands}
        template_path = "helpdesk/pages/support_list_by_technical.html"

        return render(
            request,
            template_path,
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
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # print("ID:::", id)
        demand = get_object_or_404(Demand, pk=id)
        # demand = get_object_or_404(Demand, pk=id)
        # print(demand)
        form_view = SupportFormUpdateView(request.POST or None, instance=demand)
        form = SupportFormUpdate(request.POST or None, instance=demand)

        form_view.fields["user_name"].widget.attrs["disabled"] = True
        form_view.fields["category"].widget.attrs["disabled"] = True
        form_view.fields["title"].widget.attrs["disabled"] = True
        form_view.fields["description"].widget.attrs["disabled"] = True

        # histórico
        form_historic = HistoricFormAdd(request.POST or None)
        form_historic.fields["demand_id"].initial = id
        form_historic.fields["demand_id"].widget = forms.HiddenInput()

        historic = Historic.objects.filter(demand_id=id)
        # print(historic)

        context = {
            "form": form,
            "form_view": form_view,
            "form_historic": form_historic,
            "historic": historic,
        }
        template_path = "helpdesk/pages/support_update_demand.html"

        if form.is_valid():
            form.save()
            return redirect("support_list_all")

        if form_historic.is_valid():
            form_historic.clean()
            form_historic.save()

        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise
