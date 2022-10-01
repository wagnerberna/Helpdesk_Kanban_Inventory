from django.http import HttpResponse
from django.shortcuts import render
from helpdesk.api.viewsets import DemandViewSet

demand_view_set = DemandViewSet()


# Create your views here.
def home(request):
    try:
        all_demands = demand_view_set.get_all(request)
        # print(all_demands)

        context = {"title": "HelpDesk", "all_demands": all_demands}

        return render(
            request,
            "helpdesk/pages/home.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


def about(request):
    return HttpResponse("Sistema TI de Helpdesk")
