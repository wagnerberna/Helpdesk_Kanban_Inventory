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
        fields = ["title", "project", "category", "task_owner", "status", "description"]
        labels = {
            "title": "Título:",
            "project": "Projeto:",
            "category": "Categoria:",
            "task_owner": "Dono da Tarefa:",
            "status": "Status:",
            "description": "Descrição:",
        }


class KanbanStatus(ModelForm):
    class Meta:
        model = Task
        fields = ["status"]
