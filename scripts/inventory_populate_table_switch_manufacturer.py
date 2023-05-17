import pandas
from inventory.models import Switch, SwitchHardware, SwitchManufacturer, SwitchModel


def run():
    try:
        path_file = "doc/populate_inventory/switch_fabricante.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)

            SwitchManufacturer.objects.create(
                name=row.fabricante,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
