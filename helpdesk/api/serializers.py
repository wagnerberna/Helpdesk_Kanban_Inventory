import django_filters
from django.contrib.auth.models import User
from helpdesk.models import Category, Demand, Status, Support
from rest_framework import serializers


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"


class DemandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DemandFilterSerializer(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título:")
    category = django_filters.ModelChoiceFilter(
        label="Categoria:", queryset=Category.objects.all()
    )
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição:")
    attendant = django_filters.ModelChoiceFilter(
        queryset=Support.objects.all(), label="Técnico:"
    )
    solution = django_filters.CharFilter(lookup_expr="icontains", label="Solução:")

    class Meta:
        model = Demand

        fields = (
            "title",
            "category",
            "description",
            "attendant",
            "solution",
        )


class SupportFilterSerializer(django_filters.FilterSet):
    user_name = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(), label="Nome:"
    )
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título:")
    category = django_filters.ModelChoiceFilter(
        label="Categoria:", queryset=Category.objects.all()
    )
    attendant = django_filters.ModelChoiceFilter(
        label="Técnico:", queryset=Support.objects.all()
    )
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição:")
    solution = django_filters.CharFilter(lookup_expr="icontains", label="Solução:")

    class Meta:
        model = Demand
        fields = (
            "id",
            "user_name",
            "title",
            "category",
            "description",
            "attendant",
            "status",
            "solution",
        )
