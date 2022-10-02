from multiprocessing import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from helpdesk.api.viewsets import DemandFilterViewSet, DemandViewSet, UserViewSet
from helpdesk.forms import DemandFormCreate, DemandFormUpdate

demand_view_set = DemandViewSet()
demand_filter_view_set = DemandFilterViewSet()
user_view_set = UserViewSet()

# pesquisa busca pelo name e se não encontrar passa None
# @login_required
# def demand_view_list_all(request):
#     try:
#         demands = demand_view_set.get_all(request)

#         context = {"all_demands": demands}

#         return render(
#             request,
#             "helpdesk/pages/demand_list_all.html",
#             context,
#         )
#     except Exception as error:
#         print("Internal error:", error)
#         raise


@login_required
def demand_view_list_by_user(request):
    try:
        user_id = request.user.pk
        user_name = request.user.username

        print("REQUEST::::", user_id, user_name)

        demands = demand_view_set.get_by_user_id(user_id)
        print("Demands:::", demands)

        context = {"demands": demands}

        return render(
            request,
            "helpdesk/pages/demand_list_user.html",
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
def demand_view_create(request):
    try:
        form = DemandFormCreate(request.POST or None, request.FILES or None)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("demands_list_by_user")

        return render(request, "helpdesk/pages/demand_create.html", context)

    except Exception as error:
        print("Internal error:", error)
        raise


# passa uma instância
# @login_required
# def demand_view_update(request, id):
#     try:
#         print("ID:::", id)
#         demand = demand_view_set.get_by_id(id)
#         # demand = get_object_or_404(Demand, pk=id)
#         # print(demand)
#         form = DemandFormUpdate(request.POST or None, instance=demand)

#         if form.is_valid():
#             form.save()
#             return redirect("demands_list_by_user")

#         return render(request, "helpdesk/pages/demand_update.html", {"form": form})
#     except Exception as error:
#         print("Internal error:", error)
#         raise


@login_required
def demand_view_delete(request, id):
    try:
        demand = demand_view_set.get_by_id(id)
        context = {"demand": demand}

        if request.method == "POST":
            demand.delete()
            return redirect("demands_list_by_user")

        return render(request, "helpdesk/pages/demand_delete.html", context)
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_details(request, id):
    try:
        demand = demand_view_set.get_by_id(id)
        context = {"demand": demand}

        return render(request, "helpdesk/pages/demand_details.html", context)
    except Exception as error:
        print("Internal error:", error)
        raise


# @login_required
# def demand_view_list_support(request):
#     try:
#         user_id = request.user.pk

#         # print("REQUEST::::", user_id, user_name)

#         all_demands = demand_view_set.get_by_support(user_id)
#         print(all_demands)

#         context = {"all_demands": all_demands}

#         return render(
#             request,
#             "helpdesk/pages/demand_list_all.html",
#             context,
#         )
#     except Exception as error:
#         print("Internal error:", error)
#         raise
