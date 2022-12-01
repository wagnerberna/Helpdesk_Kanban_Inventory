import math

import pandas
from django.contrib.auth.models import User
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/projects_tasks.xlsx"
        df = pandas.read_excel(path_file)
        # print(df)
        for index, row in df.iterrows():
            print(row)
            # print(index, row)
            # print(index, row.task, row.status)

            title_table = row.titulo
            project_table = row.projeto
            category_table = row.categoria
            task_owner_table = row.responsavel
            status_table = row.status
            description_table = row.descricao

            project_id_find = Project.objects.filter(name=project_table)
            project_id = project_id_find.values("id")[0].get("id")
            print(project_table, project_id)

            category_id_find = Category.objects.filter(name=category_table)
            category_id = category_id_find.values("id")[0].get("id")
            print(category_table, category_id)

            status_id_find = Status.objects.filter(name=status_table)
            status_id = status_id_find.values("id")[0].get("id")
            print(status_table, status_id)

            print("task_owner_table:::", task_owner_table)
            if math.isnan(task_owner_table):
                print("ELSE!!!!")
                # task_owner_id = None

                Task.objects.create(
                    title=title_table,
                    project=Project.objects.get(id=project_id),
                    category=Category.objects.get(id=category_id),
                    # task_owner=None,
                    status=Status.objects.get(id=status_id),
                    description=description_table,
                )

            else:
                user_task_owner_id_find = User.objects.filter(username=task_owner_table)
                user_task_owner_id = user_task_owner_id_find.values("id")[0].get("id")
                print(task_owner_table, user_task_owner_id)

                task_owner_id_find = Team.objects.filter(user_name=user_task_owner_id)
                task_owner_id = task_owner_id_find.values("id")[0].get("id")

                print(task_owner_table, task_owner_id)

                Task.objects.create(
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
