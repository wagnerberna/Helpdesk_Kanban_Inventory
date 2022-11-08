from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from kanban.api.serializers import ProjectFilterSerializer
from kanban.forms import ProjectForm
from kanban.models import Project, Team
from kanban.service.check_user_access import check_user_access


@login_required
def project_view_create(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        form = ProjectForm(request.POST or None)
        context = {"form": form}
        template_path = "kanban/pages/project_create.html"

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
def project_view_open(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects = Project.objects.all().order_by("-id").exclude(status__name="DONE")
        projects_filter = ProjectFilterSerializer(request.GET, queryset=projects)

        context = {"projects": projects, "projects_filter": projects_filter}
        template_path = "kanban/pages/project_open_list.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def project_view_done(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        projects = Project.objects.filter(status__name="DONE").order_by("-id")
        projects_filter = ProjectFilterSerializer(request.GET, queryset=projects)

        context = {"projects": projects, "projects_filter": projects_filter}
        template_path = "kanban/pages/project_done_list.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def project_view_update(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        project = get_object_or_404(Project, pk=id)

        form = ProjectForm(request.POST or None, instance=project)

        context = {"form": form}
        template_path = "kanban/pages/project_update.html"

        if form.is_valid():
            form.save()
            return redirect("project_open_filter")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def project_view_delete(request, id):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        project = get_object_or_404(Project, pk=id)
        context = {"project": project}
        template_path = "kanban/pages/project_delete.html"

        if request.method == "POST":
            project.delete()
            return redirect("project_open_filter")

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
