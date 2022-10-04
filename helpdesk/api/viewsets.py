from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from helpdesk.api.serializers import DemandSerializer, UserSerializer
from helpdesk.models import Demand
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# ordernar por ID decrescente
class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all().order_by("-id")
    serializer_class = DemandSerializer

    def get_all(self, request):
        queryset = Demand.objects.all().order_by("-id")
        return queryset

    # get_object_or_404 tenta recuperar objeto ou retorna 404

    def get_by_id(self, id):
        queryset = get_object_or_404(Demand, pk=id)
        # print("!!!queryset::: ", queryset)
        return queryset

    def get_by_user_id(self, user_id):
        queryset = Demand.objects.filter(user_name=user_id)
        print("QUERY:::", queryset)
        return queryset

    def get_by_support(self, user_id):
        queryset = Demand.objects.filter(attendant=user_id)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer

    def get_user_by_name(self, user_name):
        queryset = User.objects.filter(username=user_name)
        return queryset


# __icontains


class DemandFilterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer

    def get_by_user_name(self, user_name):
        print("MODEL!!!")

        queryset = Demand.objects.filter(username=user_name)
        return queryset
