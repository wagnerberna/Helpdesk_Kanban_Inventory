from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from helpdesk.api.viewsets import DemandFilterViewSet, DemandViewSet, UserViewSet
from helpdesk.forms import SupportFormUpdate, SupportFormUpdateView

demand_view_set = DemandViewSet()
demand_filter_view_set = DemandFilterViewSet()
user_view_set = UserViewSet()

# pesquisa busca pelo name e se não encontrar passa None
@login_required
def support_view_list_all(request):
    try:
        user_id = request.user.pk
        user_name = request.user.username

        search_input = request.GET.get("search_input", None)
        search_field = request.GET.get("search_field", None)
        print("!!!Busca!!!", search_input, search_field)

        if search_input and search_field:
            if search_field == "id":
                demands = demand_view_set.get_by_id(search_input)
                print("id find:::", demands)
            if search_field == "user_name":
                user_find = user_view_set.get_user_by_name(search_input)
                print("---user find:::", user_find)
                demands = demand_view_set
                # print(user_find.id)
                # demands = demand_filter_view_set.get_by_user_name(user_find)
            if search_field == "title":
                demands = demand_view_set.get_by_user_id(search_input)
            if search_field == "description":
                demands = demand_view_set.get_by_user_id(search_input)
            if search_field == "category":
                demands = demand_view_set.get_by_user_id(search_input)
            if search_field == "attendant":
                demands = demand_view_set.get_by_user_id(search_input)
            if search_field == "status":
                demands = demand_view_set.get_by_user_id(search_input)
            if search_field == "solution":
                demands = demand_view_set.get_by_user_id(search_input)

        else:
            demands = demand_view_set.get_all(request)
        # print(all_demands)

        context = {"all_demands": demands}

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

        context = {"form": form, "form_view": form_view}

        if form.is_valid():
            form.save()
            return redirect("support_list_all")

        return render(request, "helpdesk/pages/support_update_demand.html", context)
    except Exception as error:
        print("Internal error:", error)
        raise
