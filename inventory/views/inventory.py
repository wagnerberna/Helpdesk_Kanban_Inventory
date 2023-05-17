# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access
from inventory.api.serializers import (
    InventoryFilterSerializer,
    ServerFilterSerializer,
    SwitchFilterSerializer,
    Switch,
)

from inventory.models import (
    Inventory,
    Server,
)


@login_required
def inventory_view_workstation(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        data = Inventory.objects.all()
        # print(data[0].hardware)
        # print(data[0].hardware.cpu_model)

        inventory_filter = InventoryFilterSerializer(request.GET, queryset=data)

        context = {"data": inventory_filter.qs, "inventory_form": inventory_filter}
        template_path = "inventory/pages/inventory_workstation.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def inventory_view_server(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        data = Server.objects.all()

        server_filter = ServerFilterSerializer(request.GET, queryset=data)

        # print(server_filter.qs)

        context = {"data": server_filter.qs, "form_filter": server_filter}
        template_path = "inventory/pages/inventory_server.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def inventory_view_switch(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        data = Switch.objects.all()

        switch_filter = SwitchFilterSerializer(request.GET, queryset=data)

        # print(switch_filter.qs)

        context = {"data": switch_filter.qs, "form_filter": switch_filter}
        template_path = "inventory/pages/inventory_switch.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
