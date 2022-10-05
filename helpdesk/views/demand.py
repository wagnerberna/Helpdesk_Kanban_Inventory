from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.forms import DemandFormCreate, DemandFormUpdate
from helpdesk.models import Demand


@login_required
def demand_view_list_by_user(request):
    try:
        id = request.user.pk
        user_name = request.user.username

        # print("REQUEST::::", user_id, user_name)

        demands = Demand.objects.filter(user_name=id)
        # print("Demands:::", demands)

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
        user_id = request.user.pk
        form = DemandFormCreate(request.POST or None, request.FILES or None)
        form.fields["user_name"].initial = user_id
        form.fields["user_name"].widget = forms.HiddenInput()

        context = {"form": form}

        if form.is_valid():
            form.save()
            return redirect("demands_list_by_user")

        return render(request, "helpdesk/pages/demand_create.html", context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_details(request, id):
    try:
        # print("ID:::", id)

        demand = get_object_or_404(Demand, pk=id)
        # user_id = request.user.pk
        form = DemandFormUpdate(request.POST or None, instance=demand)
        form.fields["user_name"].widget = forms.HiddenInput()
        form.fields["category"].widget.attrs["disabled"] = True
        form.fields["title"].widget.attrs["disabled"] = True
        form.fields["description"].widget.attrs["disabled"] = True
        form.fields["attendant"].widget.attrs["disabled"] = True
        form.fields["status"].widget.attrs["disabled"] = True
        form.fields["solution"].widget.attrs["disabled"] = True

        context = {"form": form}

        return render(request, "helpdesk/pages/demand_details.html", context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_delete(request, id):
    try:
        demand = get_object_or_404(Demand, pk=id)
        context = {"demand": demand}

        if request.method == "POST":
            demand.delete()
            return redirect("demands_list_by_user")

        return render(request, "helpdesk/pages/demand_delete.html", context)
    except Exception as error:
        print("Internal error:", error)
        raise
