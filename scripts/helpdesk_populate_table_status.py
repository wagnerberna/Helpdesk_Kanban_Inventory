import pandas
from helpdesk.models import Category, Status, Support


def run():
    try:
        path_file = "doc/populate/helpdesk_status.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            # print(index, row)
            print(index, row.status)

            Status.objects.create(
                name=row.status,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
