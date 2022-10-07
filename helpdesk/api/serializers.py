import django_filters
from django.contrib.auth.models import User
from helpdesk.models import Demand, Status
from rest_framework import serializers


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        # fields = ["user_name", "status"]
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
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    solution = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Demand
        fields = (
            "title",
            "category",
            "description",
            "attendant",
            "solution",
        )
        # labels = {
        #     "title": "Título:",
        #     "category": "Categoria:",
        #     "description": "Descrição:",
        #     "attendant": "Técnico:",
        #     "solution": "Solução",
        # }


class SupportFilterSerializer(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    solution = django_filters.CharFilter(lookup_expr="icontains")

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
