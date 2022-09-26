from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.viewsets import DemandViewSet
from helpdesk.forms import DemandFormCreate, DemandFormUpdate
from helpdesk.models import Demand

demand_view_set = DemandViewSet()

# Create your views here.
@login_required
def demand_list(request):
    try:
        all_demands = demand_view_set.get_all(request)
        # print(all_demands)

        context = {"title": "Demandas", "all_demands": all_demands}

        return render(
            request,
            "helpdesk/pages/demand_list.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


# envia form importado / None para enviar o mesmo vazio
# valida formulário para salvar
# redireciona para a rota da lista pelo apelido
# Request .post pega o formulário, files as medias
@login_required
def new_demand(request):
    form = DemandFormCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("demands_list")

    return render(request, "helpdesk/pages/demand_create.html", {"form": form})


# passa uma instância
@login_required
def demand_update(request, id):
    print("ID:::", id)
    demand = demand_view_set.get_by_id(id)
    # demand = get_object_or_404(Demand, pk=id)
    print(demand)
    form = DemandFormUpdate(request.POST or None, instance=demand)

    if form.is_valid():
        form.save()
        return redirect("demands_list")

    return render(request, "helpdesk/pages/demand_update.html", {"form": form})


@login_required
def demand_delete(request, id):
    demand = demand_view_set.get_by_id(id)

    if request.method == "POST":
        demand.delete()
        return redirect("demands_list")

    return render(request, "helpdesk/pages/demand_delete.html", {"demand": demand})


def about(request):
    return HttpResponse("Sistema TI de Helpdesk")
