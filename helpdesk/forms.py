from dataclasses import Field

from django import forms
from django.forms import ModelForm
from requests import request

from .models import Demand


# importa model para criar o formulário
class DemandFormCreate(ModelForm):
    class Meta:
        model = Demand
        fields = ["user_name", "category", "title", "description", "image"]
        labels = {
            "user_name": "Nome",
            "category": "Categoria:",
            "title": "Título:",
            "description": "Descrição:",
            "image": "Imagem:",
        }
        # widget = {"user_name": forms.HiddenInput()}


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
        labels = {
            "user_name": "Nome",
            "category": "Categoria:",
            "title": "Título:",
            "description": "Descrição:",
            "image": "Imagem:",
            "attendant": "Técnico:",
            "status": "Status:",
            "solution": "Solução",
        }
