from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from kanban.forms import TaskForm
from kanban.models import Task
from kanban.service.check_user_access import check_user_access


@login_required
def task_view_create(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        form = TaskForm(request.POST or None)
        context = {"form": form}
        template_path = "kanban/pages/task_create.html"

        if form.is_valid():
            form.save()
            return redirect("kanban_manager")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
