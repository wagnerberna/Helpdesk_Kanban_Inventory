import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/populate/projects_status.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)
            print(index, row.status)

            status_table = row.status

            Status.objects.create(
                name=status_table,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
