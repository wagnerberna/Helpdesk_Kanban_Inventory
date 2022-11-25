import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/projects_names.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            # print(index, row)
            print(index, row.project, row.status)

            Project.objects.create(
                name=row.project,
                status=Status.objects.get(id=row.status),
                description=row.description,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
