import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/category.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            # print(index, row)
            print(index, row.category)

            Project.objects.create(
                name=row.category,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
