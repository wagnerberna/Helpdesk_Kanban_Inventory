import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/tasks.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            # print(index, row)
            print(index, row.task, row.status)

            Project.objects.create(
                title=row.task,
                project=Project.objects.get(id=row.status),
                category=Category.objects.get(id=row.status),
                task_owner=Team.objects.get(id=row.status),
                status=Status.objects.get(id=row.status),
                description=row.description,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
