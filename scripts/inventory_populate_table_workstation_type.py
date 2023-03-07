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
    OperationalSystem,
    Ranking,
    Software,
    SystemArchitecture,
    WorkstationManufacturer,
    WorkstationModel,
    WorkstationType,
)


def run():
    try:
        path_file = "doc/populate_inventory/estacoes_tipo.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)

            WorkstationType.objects.create(
                name=row.tipo,
            )

    except Exception as error:
        print("Internal error:", error)
        raise
