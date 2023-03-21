import pandas
from inventory.models import (
    CpuDescription,
    CpuGeneration,
    CpuManufacturer,
    CpuModel,
    HardDiskSize,
    Hardware,
    Inventory,
    Invoice,
    MemorySize,
    OperationalSystemVersion,
    Ranking,
    Software,
    SystemArchitecture,
    WorkstationManufacturer,
    WorkstationModel,
    WorkstationType,
)


def run():
    try:
        path_file = "doc/populate_inventory/so_version.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)

            OperationalSystemVersion.objects.create(
                name=row.version,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
