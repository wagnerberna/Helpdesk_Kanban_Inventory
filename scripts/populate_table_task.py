import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/project_tasks.xlsx"
        df = pandas.read_excel(path_file)
        # print(df)
        for index, row in df.iterrows():
            # print(index, row)
            # print(index, row.task, row.status)

            title_table = row.Titulo
            project_table = row.Projeto
            category_table = row.Grupo
            task_owner_table = row.Responsavel
            status_table = row.Status
            description_table = row.descricao

            project_id_find = Project.objects.filter(name=project_table)
            project_id = project_id_find.values("id")[0].get("id")

            category_id_find = Category.objects.filter(name=category_table)
            category_id = category_id_find.values("id")[0].get("id")

            task_owner_id_find = Team.objects.filter(name=task_owner_table)
            task_owner_id = task_owner_id_find.values("id")[0].get("id")

            status_id_find = Status.objects.filter(name=status_table)
            status_id = status_id_find.values("id")[0].get("id")

            Project.objects.create(
                title=title_table,
                project=Project.objects.get(id=project_id),
                category=Category.objects.get(id=category_id),
                task_owner=Team.objects.get(id=task_owner_id),
                status=Status.objects.get(id=status_id),
                description=description_table,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
