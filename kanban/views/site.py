from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        "kanban/pages/home.html",
        context={"title": "Kanban"},
    )


def about(request):
    return HttpResponse("Sistema TI de Projetos Kanban")
