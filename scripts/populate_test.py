import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        # adicionar dado ao bd pelo ID da chave estrangeira:
        Project.objects.create(
            name="Teste2", status=Status.objects.get(id=4), description="blablabla"
        )

        # adicionar dado ao bd pelo valor da chave estrangeira:
        status = Status.objects.filter(name="TO DO")
        print(status)
        # <QuerySet [<Status: TO DO>]>
        print(status.values("name"))
        # <QuerySet [{'name': 'TO DO'}]>
        print(status.values("id"))
        # <QuerySet [{'id': 1}]>
        print(status.values("id")[0])
        # {'id': 1}
        print(status.values("id")[0].get("id"))
        #  1

        status_add = status.values("id")[0].get("id")

        Project.objects.create(
            name="Teste5",
            status=Status.objects.get(id=status_add),
            description="blablabla",
        )

    # owner = Task.objects.filter(task_owner__user_name="wagner.berna")

    # print("owner:::", owner)
    # project_id = Task.objects.filter(project__name="Padronização Workstations")

    # print("project_id:::", project_id)

    except Exception as error:
        print("Internal error:", error)
        raise
