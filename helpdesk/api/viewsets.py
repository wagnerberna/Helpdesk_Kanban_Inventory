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
