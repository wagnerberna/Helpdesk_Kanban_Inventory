import pandas
from ti.models import Department


def run():
    try:
        path_file = "doc/populate/ti_department.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            # print(index, row)
            print(index, row.setor)

            Department.objects.create(
                name=row.setor,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
