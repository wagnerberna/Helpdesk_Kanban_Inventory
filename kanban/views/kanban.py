from django.shortcuts import render


def manager(request):
    return render(
        request,
        "kanban/pages/kanban_manager.html",
        context={"title": "Kanban"},
    )
