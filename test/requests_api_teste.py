import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)

    # consultar API externa requests
    response = requests.get("http://localhost:8000/helpdesk/api/demand/").json()
    print(response)
    return render(
        request,
        "helpdesk/pages/home.html",
        context={"title": "HelpDesk", "response": response},
    )


def about(request):
    return HttpResponse("Sistema TI de Helpdesk")
