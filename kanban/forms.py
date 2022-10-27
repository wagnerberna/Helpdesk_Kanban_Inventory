from django.forms import ModelForm

from .models import Project


class ProjectFormCreate(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "status", "description"]
        labels = {
            "name": "Nome do Projeto:",
            "status": "Status:",
            "description": "Descrição:",
        }


# class ProjectFormUpdate(ModelForm):
#     class Meta:
#         model = Project
#         fields = ["name", "status", "description"]
