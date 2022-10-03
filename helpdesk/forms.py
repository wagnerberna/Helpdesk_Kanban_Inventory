from dataclasses import Field

from django import forms
from django.forms import ModelForm

from .models import Demand


# importa model para criar o formulário
class DemandFormCreate(ModelForm):
    class Meta:
        model = Demand
        fields = ["user_name", "category", "title", "description", "image"]


class DemandFormUpdate(ModelForm):
    class Meta:
        model = Demand
        fields = [
            "user_name",
            "category",
            "title",
            "description",
            "image",
            "attendant",
            "status",
            "solution",
        ]
