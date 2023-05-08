import django_filters
from kanban.models import Category, Project, Task, Team, Priority
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class ProjectFilterSerializer(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Nome:")
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição:")

    class Meta:
        model = Project
        fields = ("id", "name", "status", "description")


class TaskFilterSerializer(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título:")
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição:")
    project = django_filters.ModelChoiceFilter(
        label="Projeto:", queryset=Project.objects.all()
    )
    category = django_filters.ModelChoiceFilter(
        label="Categoria:", queryset=Category.objects.all()
    )
    task_owner = django_filters.ModelChoiceFilter(
        label="Dono da Tarefa:", queryset=Team.objects.all()
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "project",
            "category",
            "task_owner",
            "status",
            "description",
        )


class KanbanFilterSerializer(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título:")
    task_owner = django_filters.ModelChoiceFilter(
        label="Dono da Tarefa:", queryset=Team.objects.all()
    )
    priority = django_filters.ModelChoiceFilter(
        label="Prioridade da Tarefa:", queryset=Priority.objects.all()
    )

    class Meta:
        model = Task
        fields = (
            "title",
            "task_owner",
            "priority",
        )
