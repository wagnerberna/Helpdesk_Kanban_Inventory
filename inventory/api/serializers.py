import django_filters

# from django.contrib.auth.models import User
from rest_framework import serializers
from inventory.models import (
    Inventory,
    Ranking,
    StatusSituation,
    Server,
    Software,
    SwitchHardware,
    Switch,
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


class SwitchFilterSerializer(django_filters.FilterSet):
    inventory = django_filters.CharFilter(lookup_expr="icontains", label="Patrimônio:")
    switch_hardware = django_filters.ModelChoiceFilter(
        queryset=SwitchHardware.objects.all(), label="Marca e Modelo:"
    )
    ip = django_filters.CharFilter(lookup_expr="icontains", label="Endereço IP:")
    mac = django_filters.CharFilter(lookup_expr="icontains", label="Endereço MAC:")
    status = django_filters.ModelChoiceFilter(
        queryset=StatusSituation.objects.all(), label="Status:"
    )
    department = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all(), label="Setor:"
    )

    class Meta:
        model = Switch

        fields = ("inventory", "switch_hardware", "ip", "mac", "status", "department")
