import pandas
from inventory.models import ServerStatus


def run():
    try:
        path_file = "doc/populate_inventory/server_status.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)

            ServerStatus.objects.create(
                name=row.status,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
