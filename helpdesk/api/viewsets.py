import django_filters
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from helpdesk.api.serializers import (
    DemandFilterSerializer,
    DemandSerializer,
    StatusSerializer,
    UserSerializer,
)
from helpdesk.models import Demand, Status
from rest_framework import viewsets
from rest_framework.decorators import action


# ordernar por ID decrescente
class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all().order_by("-id")
    serializer_class = DemandSerializer

    # def get_all(self):
    #     queryset = Demand.objects.all().order_by("-id")
    #     return queryset

    # get_object_or_404 tenta recuperar objeto ou retorna 404

    # def get_by_id(self, id):
    #     queryset = get_object_or_404(Demand, pk=id)
    #     # print("!!!queryset::: ", queryset)
    #     return queryset

    # def get_by_user_id(self, user_id):
    #     queryset = Demand.objects.filter(user_name=user_id)
    #     print("QUERY:::", queryset)
    #     return queryset

    # def get_by_support(self, user_id):
    #     queryset = Demand.objects.filter(attendant=user_id)
    #     return queryset


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by("-id")
#     serializer_class = UserSerializer

#     def get_id_by_name(self, user_name):
#         queryset = User.objects.filter(username=user_name)
#         return queryset


# class StatusViewSet(viewsets.ModelViewSet):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def get_id_by_status_name(self, status_name):
#         queryset = Status.objects.filter(name=status_name)
#         print("QUERYSET STATUS:::", queryset)
#         return queryset


# class DemandFilterViewSet(viewsets.ModelViewSet):
#     queryset = Demand.objects.all().order_by("-id")
#     serializer_class = DemandFilterSerializer

# def demand_list_by_title(self, title):
#     queryset = Demand.


# def get_by_status(self, status):
#     print("MODEL!!!")

#     queryset = Demand.objects.filter(status=status)
#     return queryset
