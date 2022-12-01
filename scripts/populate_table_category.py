import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/projects_category.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)
            print(index, row.categoria, row.descricao)

            Category.objects.create(
                name=row.categoria,
                description=row.descricao,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
