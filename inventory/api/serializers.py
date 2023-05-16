import django_filters

# from django.contrib.auth.models import User
from rest_framework import serializers
from inventory.models import Inventory, Ranking, StatusSituation
from ti.models import Department


class InventoryFilterSerializer(django_filters.FilterSet):
    inventory = django_filters.CharFilter(lookup_expr="icontains", label="Patrimônio:")
    hostname = django_filters.CharFilter(lookup_expr="icontains", label="hostname:")
    department = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all(), label="Setor:"
    )
    ranking = django_filters.ModelChoiceFilter(
        queryset=Ranking.objects.all(), label="Setor:"
    )
    status = django_filters.ModelChoiceFilter(
        queryset=StatusSituation.objects.all(), label="Status:"
    )

    class Meta:
        model = Inventory

        fields = ("inventory", "hostname", "department", "ranking", "status")
