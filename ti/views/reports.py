import base64
import io
import urllib

import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.serializers import SupportFilterSerializer
from helpdesk.forms import SupportFormUpdate, SupportFormUpdateView
from helpdesk.models import Demand, Support
from helpdesk.service.check_user_access import check_user_access


@login_required
def reports(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        demmands_leonardo = Demand.objects.filter(attendant__user_name=4).count()
        demmands_wagner = Demand.objects.filter(attendant__user_name=2).count()

        # print("Demandas LEO:::", demmands_leonardo)
        techinicals = ["Leonardo", "Wagner"]
        total_demands = [demmands_leonardo, demmands_wagner]
        plt.bar(techinicals, total_demands, color="blue")

        plt.title("Chamados por Técnico")
        fig = plt.gcf()
        # convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read())

        # Teste gráfico 2:
        # demmands_leonardo = Demand.objects.filter(attendant__user_name=4).count()
        # demmands_wagner = Demand.objects.filter(attendant__user_name=2).count()

        # print("Demandas LEO:::", demmands_leonardo)
        # techinicals = ["Leonardo", "Wagner"]
        # total_demands = [100, 200]
        # plt.bar(techinicals, total_demands, color="red")

        # plt.title("Projetos")
        # fig2 = plt.gcf()
        # buf2 = io.BytesIO()
        # fig2.savefig(buf, format="png")
        # buf2.seek(0)
        # string2 = base64.b64encode(buf.read())

        context = {
            "data": urllib.parse.quote(string),
            # "data2": urllib.parse.quote(string2),
        }

        # return render(request,'home.html',{'data':uri})

        #     demands = Demand.objects.filter(status__name="Finalizado").order_by("-id")
        #     demand_filter = SupportFilterSerializer(request.GET, queryset=demands)

        #     # print(demand_filter)
        #     context = {"all_demands": demands, "demand_filter": demand_filter}
        template_path = "ti/pages/reports.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise
