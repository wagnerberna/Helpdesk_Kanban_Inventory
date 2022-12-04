from django import forms
from django.forms import ModelForm

from .models import Demand, Historic


# model usado para criar o formulário
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


class SupportFormUpdateView(ModelForm):
    class Meta:
        model = Demand
        fields = [
            "user_name",
            "category",
            "title",
            "description",
            "image",
        ]
        labels = {
            "user_name": "Nome",
            "category": "Categoria:",
            "title": "Título:",
            "description": "Descrição:",
            "image": "Imagem:",
        }


class SupportFormUpdate(ModelForm):
    class Meta:
        model = Demand
        fields = [
            "attendant",
            "status",
            "solution",
        ]
        # widgets = {"solutin": forms.TextInput}
        labels = {
            "attendant": "Técnico:",
            "status": "Status:",
            "solution": "Solução",
        }


class HistoricFormAdd(ModelForm):
    class Meta:
        model = Historic
        fields = ["demand_id", "historic"]
        labels = {"historic": "Histórico:"}
