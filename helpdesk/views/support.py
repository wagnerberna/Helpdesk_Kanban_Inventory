from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.serializers import SupportFilterSerializer
from helpdesk.forms import SupportFormUpdate, SupportFormUpdateView
from helpdesk.models import Demand, Support

#  <QuerySet [<Support: wagner.berna>]>
# print("check:::", check.values("user_name")[0])

# Retorna erro 404
# @login_required
# def check_user_permission(request):
#     id = request.user.pk
#     check = get_object_or_404(Support, user_name=id)
#     return check


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Support.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True


@login_required
def support_view_list_all(request):
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
        template_path = "helpdesk/pages/support_list_all_demand.html"

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

        print(demand_filter)
        context = {"all_demands": demands, "demand_filter": demand_filter}
        template_path = "helpdesk/pages/support_list_all_demand.html"

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
        template_path = "helpdesk/pages/support_list_technical_demand.html"

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

        # template =
        context = {"form": form, "form_view": form_view}
        template_path = "helpdesk/pages/support_update_demand.html"

        if form.is_valid():
            form.save()
            return redirect("support_list_all")

        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise
