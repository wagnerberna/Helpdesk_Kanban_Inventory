from django.shortcuts import get_object_or_404
from helpdesk.api.serializers import DemandSerializer
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

    def get_by_user(self, user):

        queryset = Demand.objects.filter(user_name=user)
        print("QUERY:::", queryset)
        return queryset
