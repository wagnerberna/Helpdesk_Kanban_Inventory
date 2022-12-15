import pandas
from helpdesk.models import Category, Status, Support


def run():
    try:
        path_file = "doc/populate/helpdesk_category.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)
            print(index, row.categoria)

            Category.objects.create(
                name=row.categoria,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
