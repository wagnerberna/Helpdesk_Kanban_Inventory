# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access
from inventory.api.serializers import InventoryFilterSerializer

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

        context = {"data": data}
        template_path = "inventory/pages/inventory_server.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
