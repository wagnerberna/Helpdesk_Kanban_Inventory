import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        # adicionar dado ao bd:
        # Project.objects.create(
        #     name="Teste2", status=Status.objects.get(id=4), description="blablabla"
        # )

        # owner = Task.objects.filter(task_owner__user_name="wagner.berna")

        # print("owner:::", owner)
        project_id = Task.objects.filter(project__name="Padronização Workstations")

        print("project_id:::", project_id)

    except Exception as error:
        print("Internal error:", error)
        raise
