from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access

from inventory.models import (
    CpuDescription,
    CpuGeneration,
    CpuManufacturer,
    CpuModel,
    HardDiskSize,
    Hardware,
    Inventory,
    Invoice,
    MemorySize,
    OperationalSystem,
    Ranking,
    Software,
    SystemArchitecture,
    WorkstationManufacturer,
    WorkstationModel,
    WorkstationType,
)


@login_required
def inventory_view_list_all(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        data = Inventory.objects.all()
        # print(data[0].hardware)
        # print(data[0].hardware.cpu_model)

        context = {"data": data}
        template_path = "inventory/pages/inventory_list_all.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
