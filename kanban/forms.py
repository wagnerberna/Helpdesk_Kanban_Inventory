from django import forms
from django.forms import ModelForm

from .models import Project, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "status", "description"]
        labels = {
            "name": "Nome do Projeto:",
            "status": "Status:",
            "description": "Descrição:",
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "project",
            "category",
            "task_owner",
            "status",
            "priority",
            "description",
        ]
        labels = {
            "title": "Título:",
            "project": "Projeto:",
            "category": "Categoria:",
            "task_owner": "Dono da Tarefa:",
            "status": "Status:",
            "priority": "Prioridade",
            "description": "Descrição:",
        }


class KanbanStatusFormNext(forms.Form):
    id_task = forms.CharField(required=False)
