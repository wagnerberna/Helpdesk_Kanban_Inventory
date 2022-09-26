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
        print("!!!queryset::: ", queryset)
        return queryset

    # def get_by_id(self, id):
    #     queryset = Demand.objects.filter(pk=id)
    #     return queryset

    # @action(detail=True, methods=["get"])
    # def list(self, request, pk=None, *args, **kwargs):
    #     queryset = Demand.objects.filter(pk=pk)
    #     self.serializer_class = DemandSerializer
    #     serializer = self.get_serializer(queryset)
    #     # print(all_demands)
    #     return Response(serializer.data)

    # def create(self, request):
    #     pass

    # # retorna apena 1 registro
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     pass
