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

            name_table = row.project
            status_table = row.status
            description_table = row.description

            status_id_find = Status.objects.filter(name=status_table)
            status_id = status_id_find.values("id")[0].get("id")
            print("STATUS ID:::", status_id)

            Project.objects.create(
                name=name_table,
                status=Status.objects.get(id=status_id),
                description=description_table,
            )

    except Exception as error:
        print("Internal error:", error)
        raise