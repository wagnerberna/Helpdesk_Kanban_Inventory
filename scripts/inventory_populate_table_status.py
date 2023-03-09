import pandas
from inventory.models import StatusSituation


def run():
    try:
        path_file = "doc/populate_inventory/status.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)

            StatusSituation.objects.create(
                name=row.status,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
