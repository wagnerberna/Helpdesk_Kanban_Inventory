from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from ti.service.check_user_access import check_user_access

from kanban.api.serializers import TaskFilterSerializer
from kanban.forms import TaskForm
from kanban.models import Task


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


@login_required
def task_view_open(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        tasks = Task.objects.all().order_by("-id").exclude(status__name="DONE")
        tasks_filter = TaskFilterSerializer(request.GET, queryset=tasks)

        context = {"tasks": tasks, "tasks_filter": tasks_filter}
        template_path = "kanban/pages/task_open_list.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


# .qs (QuerySet)
@login_required
def task_view_done(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        tasks = Task.objects.filter(status__name="DONE").order_by("-id")
        tasks_filter = TaskFilterSerializer(request.GET, queryset=tasks)

        # print("tasks", type(tasks), "LEN:::", len(tasks))
        # print("tasks_filter", type(tasks_filter))
        # print(tasks_filter.qs)

        paginator_tasks = Paginator(tasks_filter.qs, 50)
        # print(paginator_tasks.count)
        # print(paginator_tasks.num_pages)
        # print(paginator_tasks.page_range)
        # print(paginator_tasks.count)
        # print(paginator_tasks.get_page(2))

        page = request.GET.get("page")
        tasks_page = paginator_tasks.get_page(page)

        # context = {"tasks": tasks, "tasks_filter": tasks_filter}
        context = {"tasks_filter": tasks_page, "tasks_form": tasks_filter}

        template_path = "kanban/pages/task_done_list.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def task_view_update(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        task = get_object_or_404(Task, pk=id)

        form = TaskForm(request.POST or None, instance=task)

        context = {"form": form}
        template_path = "kanban/pages/task_update.html"

        if form.is_valid():
            form.save()
            return redirect("task_open_filter")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def task_view_delete(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        task = get_object_or_404(Task, pk=id)
        context = {"project": task}
        template_path = "kanban/pages/task_delete.html"

        if request.method == "POST":
            task.delete()
            return redirect("task_open_filter")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
