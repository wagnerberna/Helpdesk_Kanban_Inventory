import django_filters

# from django.contrib.auth.models import User
from rest_framework import serializers
from inventory.models import (
    Inventory,
    Ranking,
    StatusSituation,
    Server,
    OperationalSystemVersion,
    OperationalSystem,
    Software,
)
from ti.models import Department


class InventoryFilterSerializer(django_filters.FilterSet):
    inventory = django_filters.CharFilter(lookup_expr="icontains", label="Patrimônio:")
    hostname = django_filters.CharFilter(lookup_expr="icontains", label="Nome:")
    department = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all(), label="Setor:"
    )
    ranking = django_filters.ModelChoiceFilter(
        queryset=Ranking.objects.all(), label="Ranking:"
    )
    status = django_filters.ModelChoiceFilter(
        queryset=StatusSituation.objects.all(), label="Status:"
    )

    class Meta:
        model = Inventory

        fields = ("inventory", "hostname", "department", "ranking", "status")


class ServerFilterSerializer(django_filters.FilterSet):
    hostname = django_filters.ModelChoiceFilter(
        queryset=Server.objects.all(), label="Nome:"
    )
    software = django_filters.ModelChoiceFilter(
        queryset=Software.objects.all(), label="Sistema Operacional:"
    )
    ip = django_filters.CharFilter(lookup_expr="icontains", label="Endereço IP:")

    class Meta:
        model = Server

        fields = ("hostname", "software", "ip")
