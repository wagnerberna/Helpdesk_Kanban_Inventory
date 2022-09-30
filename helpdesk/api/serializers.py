from django.contrib.auth.models import User
from helpdesk.models import Demand
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
        model = User
        fields = "__all__"
